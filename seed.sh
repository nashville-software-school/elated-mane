#!/bin/bash

rm -rf levelupapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations maneapi
python manage.py migrate maneapi
python3 manage.py loaddata styles users tokens customers equipment_types equipment appointments