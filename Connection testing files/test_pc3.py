import mysql.connector

connection = mysql.connector.connect(
    host="172.16.16.0",  # Device A's IP address
    user="usman",
    password="usman123",
    database="StudentManagement"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM Student")
for row in cursor.fetchall():
    print(row)
cursor.close()