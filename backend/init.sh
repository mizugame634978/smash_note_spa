#!/usr/bin/env bash

echo "===== build.sh START ====="
# exit on error
set -o errexit

pip install -r requirements.txt

# dbが存在しないとエラーになる
python manage.py makemigrations
python manage.py migrate

# 最初の１回だけ行う・キャクターの初期化
python manage.py character_init
# dockerの方でrunserverするので使わない

echo "===== build.sh END ====="