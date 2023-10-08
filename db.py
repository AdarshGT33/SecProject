import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@mr@m",
    database="projectdb"
)

cursor = db_connection.cursor()
query = "SELECT * FROM employees"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db_connection.close()
