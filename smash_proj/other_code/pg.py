import psycopg2
# テキストファイルの内容をpostgreに入れる
#dbに接続#
pg_conn =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(
                user="testuser",        #ユーザ
                password="test",  #パスワード
                host="localhost",       #ホスト名
                port="5432",            #ポート
                dbname="testdb"))    #データベース名

f_cur = open('myfile.txt','w',encoding='UTF-8')#ファイルのカーソルを取得
pg_cur = pg_conn.cursor()#DBのカーソルを取得

##sqlを実行##
sql_str  = "select * from smash_note_character order by id"
pg_cur.execute(sql_str)

##sqlの実行結果を外部ファイルに書き込む###
for i in pg_cur.fetchall():
    f_cur.write('{')
    cnt = 1
    for j in i:
        print(str(j))
        if(cnt == 1):
            f_cur.write('"character_id":')
            f_cur.writelines(str(j))

        elif(cnt == 2):
            f_cur.write('"character_name":"')
            f_cur.writelines(str(j))
            f_cur.write('"')
        else:
            f_cur.write('"img_path":"')
            f_cur.writelines(str(j))
            f_cur.write('"')

        if(cnt <len(i)):
            f_cur.write(",")
        cnt +=   1
    f_cur.write('},\n')

pg_conn.commit()

pg_conn.close()# データベースへのコネクションを閉じる。
f_cur.close()

"""外部ファイルへの出力イメージ
{"character_id":1,"character_name":"マリオ","img_path":"images/mario.jpg"},
{"character_id":2,"character_name":"ドンキーコング","img_path":"images/donkey.jpg"},
{"character_id":3,"character_name":"リンク","img_path":"images/link.jpg"},
"""



