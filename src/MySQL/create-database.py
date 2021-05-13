import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

my_cursor = my_database.cursor()
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
my_cursor.execute("CREATE DATABASE Example")