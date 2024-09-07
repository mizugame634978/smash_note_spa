
import sqlite3

#sqlite3のものをポスグレに移す
# 標準出力をコピペしてテキストファイルを作成

conn = sqlite3.connect('../db.sqlite3')#dbに接続

cur = conn.cursor()
#cur2 = conn2.cursor()


sql_str  = "select * from smash_note_character order by id"
cur.execute(sql_str)
cur.execute(sql_str)
for i in cur.fetchall():

    for j in i:
        print(str(j))


conn.commit()

cur.close()#データベースの接続を切断

conn.close()# データベースへのコネクションを閉じる。






