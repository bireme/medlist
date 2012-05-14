import os
from django.db.models import signals
from django.conf import settings
from whoosh import store, fields, index
from search import search
from models import *
from directory.models import LANGUAGES_CHOICES

WHOOSH_SCHEMA = fields.Schema(medicine=fields.TEXT(stored=True),
                                medicine_es=fields.TEXT(stored=True),
                                medicine_pt=fields.TEXT(stored=True),
								type=fields.TEXT(stored=True),
                                type_es=fields.TEXT(stored=True),
                                type_pt=fields.TEXT(stored=True),
								composition=fields.TEXT(stored=True),
								list=fields.NUMERIC(stored=True),
								medicine_id=fields.NUMERIC(stored=True),
								id=fields.NUMERIC(stored=True, unique=True))

def create_index(sender=None, **kwargs):
    if not os.path.exists(settings.WHOOSH_INDEX):
        os.mkdir(settings.WHOOSH_INDEX)
        ix = index.create_in(settings.WHOOSH_INDEX, WHOOSH_SCHEMA)
signals.post_syncdb.connect(create_index)

def update_index(sender, instance, created, **kwargs):
    # reading the index
    ix = index.open_dir(settings.WHOOSH_INDEX)
    # creating the writer object
    writer = ix.writer()

    # if already exists, append the list in field lists.
    list_id = instance.section.list.id
    docs = search(instance.pharmaceutical_form.id, field="id")
    if docs and 'list' in docs[0]:
        if not list_id in docs[0]['list']:
            list = docs[0]['list'] 
            list.append(list_id)
        else:
            list = docs[0]['list']
    else:
        list = [list_id]

    # if don't exists, create the doc
    if not docs:
        writer.add_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            composition=instance.pharmaceutical_form.composition,
                            list=[instance.section.list.id],
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=instance.pharmaceutical_form.id)
    # if exists, update doc
    else:   
        writer.update_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            composition=instance.pharmaceutical_form.composition,
                            list=list,
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=instance.pharmaceutical_form.id)
    writer.commit()
signals.post_save.connect(update_index, sender=SectionPharmForm)

def delete_index(sender, instance, using, **kwargs):
    """
    Removes a list from lists field on doc.
    """

    ix = index.open_dir(settings.WHOOSH_INDEX)
    writer = ix.writer()
    
    docs = search(instance.pharmaceutical_form.id, field="id")
    if docs and 'list' in docs[0]:
        list = docs[0]['list']
        
        try: list.remove(instance.section.list.id) 
        except: pass

        writer.update_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            composition=instance.pharmaceutical_form.composition,
                            list=list,
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=instance.pharmaceutical_form.id)
        writer.commit()


signals.pre_delete.connect(delete_index, sender=SectionPharmForm)