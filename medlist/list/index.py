import os
from django.db.models import signals
from django.conf import settings
from whoosh import store, fields, index
from search import search
from models import *

# title=fields.TEXT(stored=True),
#    content=fields.TEXT,
#    url=fields.ID(stored=True, unique=True))
WHOOSH_SCHEMA = fields.Schema(medicine=fields.TEXT(stored=True),
								type=fields.TEXT(stored=True),
								composition=fields.TEXT(stored=True),
								list=fields.NUMERIC(stored=True),
								id=fields.NUMERIC(stored=True, unique=True))

def create_index(sender=None, **kwargs):
    if not os.path.exists(settings.WHOOSH_INDEX):
        os.mkdir(settings.WHOOSH_INDEX)
        ix = index.create_in(settings.WHOOSH_INDEX, WHOOSH_SCHEMA)
signals.post_syncdb.connect(create_index)

def update_index(sender, instance, created, **kwargs):
    ix = index.open_dir(settings.WHOOSH_INDEX)
    writer = ix.writer() 


    if created:
        writer.add_document(medicine=instance.pharmaceutical_form.medicine.name,
        					type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
        					composition=instance.pharmaceutical_form.composition,
        					list=[instance.section.list.id],
        					id=instance.pharmaceutical_form.id)
        writer.commit()
    else:   

		list_id = instance.section.list.id
		docs = search(instance.pharmaceutical_form.id, field="id")
		if docs and 'list' in docs[0]:
			if not list_id in docs[0]['list']:
				list = docs[0]['list'] 
				list.append(list_id)
			else:
				list = docs[0]['list']

		writer.update_document(medicine=instance.pharmaceutical_form.medicine.name,
							type=instance.pharmaceutical_form.pharmaceutical_form_type.name,
							composition=instance.pharmaceutical_form.composition,
							list=list,
							id=instance.pharmaceutical_form.id)
		writer.commit()
signals.post_save.connect(update_index, sender=SectionPharmForm)