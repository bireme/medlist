#!/usr/bin/env python
import os, sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medlist.settings')
django.setup()

from django.conf import settings
from whoosh import fields, index
from list.index import WHOOSH_SCHEMA
from list.models import *


if not os.path.exists(settings.WHOOSH_INDEX):
    os.mkdir(settings.WHOOSH_INDEX)
    ix = index.create_in(settings.WHOOSH_INDEX, WHOOSH_SCHEMA)

#records = SectionPharmForm.objects.filter(section__list__in=[11,12])
records = SectionPharmForm.objects.all()

for obj in records:
    print(obj.id)
    obj.save()