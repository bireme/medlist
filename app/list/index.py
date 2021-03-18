import os
from django.db.models.signals import post_save, pre_delete, post_migrate
from django.dispatch import receiver
from django.conf import settings
from whoosh import fields, index
from list.search import search
from list.models import SectionPharmForm
from directory.models import LANGUAGES_CHOICES

WHOOSH_SCHEMA = fields.Schema(medicine=fields.TEXT(stored=True),
                                medicine_es=fields.TEXT(stored=True),
                                medicine_pt=fields.TEXT(stored=True),
								type=fields.TEXT(stored=True),
                                type_es=fields.TEXT(stored=True),
                                type_pt=fields.TEXT(stored=True),
								composition=fields.TEXT(stored=True),
								list=fields.NUMERIC(stored=True),
                                comparative_type=fields.KEYWORD(stored=True),
								medicine_id=fields.NUMERIC(stored=True),
								id=fields.ID(stored=True, unique=True))

@receiver(post_migrate, sender=SectionPharmForm)
def create_index(sender=None, **kwargs):
    if not os.path.exists(settings.WHOOSH_INDEX):
        os.mkdir(settings.WHOOSH_INDEX)
        ix = index.create_in(settings.WHOOSH_INDEX, WHOOSH_SCHEMA)


@receiver(post_save, sender=SectionPharmForm)
def update_index(sender, instance, created, **kwargs):
    # reading the index
    ix = index.open_dir(settings.WHOOSH_INDEX)
    # creating the writer object
    writer = ix.writer()

    # search by doc used for complete comparison version: medicine + pharmaceutical form type + composition
    doc_id = "{}-{}".format(instance.pharmaceutical_form.id, 'complete')
    result = search(doc_id, field="id")
    # if doc exists, append current list in field list
    list_id = instance.section.list.id
    if result and 'list' in result[0]:
        if not list_id in result[0]['list']:
            in_list = result[0]['list']
            in_list.append(list_id)
        else:
            in_list = result[0]['list']
    else:
        in_list = [list_id]

    # create or update complete doc version
    if not result:
        writer.add_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            composition=instance.pharmaceutical_form.composition,
                            list=in_list,
                            comparative_type='complete',
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=doc_id)
    else:
        writer.update_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            composition=instance.pharmaceutical_form.composition,
                            list=in_list,
                            comparative_type='complete',
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=doc_id)



    # search by doc used for complete comparison version: medicine + pharmaceutical form type
    doc_id = "{}-{}".format(instance.pharmaceutical_form.medicine.id, instance.pharmaceutical_form.pharmaceutical_form_type.id)
    result = search(doc_id, field="id")
    # if doc exists, append current list in field list
    if result and 'list' in result[0]:
        if not list_id in result[0]['list']:
            in_list = result[0]['list']
            in_list.append(list_id)
        else:
            in_list = result[0]['list']
    else:
        in_list = [list_id]


    # create or update doc that allow comparison using: medicine + pharmaceutical form type
    if not result:
        writer.add_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            list=in_list,
                            comparative_type='medicine_pharmaceuticalform',
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=doc_id)
    else:
        writer.update_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
                            type_es=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('es'),
                            type_pt=instance.pharmaceutical_form.pharmaceutical_form_type.get_translation('pt-br'),
                            list=in_list,
                            comparative_type='medicine_pharmaceuticalform',
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=doc_id)





    # search by doc used for complete comparison version: medicine
    doc_id = "{}-{}".format(instance.pharmaceutical_form.medicine.id, 'medicine')
    result = search(doc_id, field="id")
    # if doc exists, append current list in field list
    if result and 'list' in result[0]:
        if not list_id in result[0]['list']:
            in_list = result[0]['list']
            in_list.append(list_id)
        else:
            in_list = result[0]['list']
    else:
        in_list = [list_id]


    # create or update doc that allow comparison using: medicine
    if not result:
        writer.add_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            list=in_list,
                            comparative_type='medicine',
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=doc_id)
    else:
        writer.update_document(medicine=instance.pharmaceutical_form.medicine.name,
                            medicine_es=instance.pharmaceutical_form.medicine.get_translation('es'),
                            medicine_pt=instance.pharmaceutical_form.medicine.get_translation('pt-br'),
                            list=in_list,
                            comparative_type='medicine',
                            medicine_id=instance.pharmaceutical_form.medicine.id,
                            id=doc_id)




    # update index
    writer.commit()


@receiver(pre_delete, sender=SectionPharmForm)
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
