import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', port = '3307', database = 'db_spksaw')

mycursor = db.cursor()

sql = "UPDATE evaluasi SET nilai = 99"

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "record(s) affected")
