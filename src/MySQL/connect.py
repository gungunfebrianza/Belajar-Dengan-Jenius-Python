import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test",
)

# print(my_database)
