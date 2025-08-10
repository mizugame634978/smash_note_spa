#!/usr/bin/env bash

echo "===== build.sh START ====="
# exit on error
set -o errexit

# pip install -r requirements.txt
# python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
# python manage.py superuser
# 最初の１回だけ行う
python manage.py character_init
# dockerの方でrunserverするので使わない
# python manage.py runserver

echo "===== build.sh END ====="