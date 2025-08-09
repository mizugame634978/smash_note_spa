import sqlite3

# 旧Dbから新DBにキャラクターデータを移行(sqlite3からpostgressに移行する際に使用)

conn = sqlite3.connect('db.sqlite3')#dbに接続
conn2 = sqlite3.connect('db2.sqlite3')#dbに接続
cur = conn.cursor()
cur2 = conn2.cursor()

sql_str  = "select * from smash_note_character"
cur2.execute(sql_str)
#print(cur2.fetchall())
for i in cur2.fetchall():
    sql_str  = "insert into smash_note_character values("+str(i[0])+",'"+i[1]+"','"+i[2]+"')"
    cur.execute(sql_str)
    #print(sql_str)


conn.commit()
conn2.commit()
cur.close()#データベースの接続を切断
cur2.close()#データベースの接続を切断
conn.close()# データベースへのコネクションを閉じる。
conn2.close()# データベースへのコネクションを閉じる。