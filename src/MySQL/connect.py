import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test",
)

# print(my_database)

my_cursor = my_database.cursor()
my_cursor.execute("SHOW DATABASES")