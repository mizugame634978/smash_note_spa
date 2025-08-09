
# インストール&起動
`bash init.sh`と実行すれば起動できるようにする予定(作成中)
```init.sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py character_init
python manage.py runserver
```

# キャラクター初期化
migrationやdb.sqliteを削除した場合、またはcloneしてDBのデータ以外をすべて設定した場合、
以下のコマンドでキャラクターデータをすべて登録できる
```shell
python manage.py character_init
```