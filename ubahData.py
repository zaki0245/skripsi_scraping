import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', port = '3307', database = 'db_spksaw')

mycursor = db.cursor()

sql = "UPDATE evaluasi SET nilai = 98 WHERE created_at IS NULL"

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "record(s) affected")
