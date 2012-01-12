#!/bin/bash

CUR=`pwd`

cd ..

python manage.py loaddata fixtures/initial_data.json
python manage.py loaddata tools/json-django/Language.json
python manage.py loaddata tools/json-django/MedicineAppStatus.json
python manage.py loaddata tools/json-django/Medicine.json
python manage.py loaddata tools/json-django/MedicineApp.json
python manage.py loaddata tools/json-django/MedicineAppType.json

python manage.py loaddata tools/json-django/MedicineAppType_Local.json
python manage.py loaddata tools/json-django/MedicineAppHistoryDate.json
python manage.py loaddata tools/json-django/Medicine_Local.json

python manage.py loaddata tools/json-django/MedicineRef.json

cd ${CUR}
