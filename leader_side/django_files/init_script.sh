#!/bin/bash
# Automatin migration and set of superuser

cd Covid_Map

python manage.py makemigrations

python manage.py migrate

#python manage.py ensure_adminuser --user=master --password=theoneaboveall

#python manage.py runserver 0.0.0.0:8000

gunicorn Covid_Map.wsgi:application --bind 0.0.0.0:8000
