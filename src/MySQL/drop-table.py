import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test",
)

my_cursor = my_database.cursor()

# DELETE DROP TABLE
my_sql = "DROP TABLE IF EXISTS users"
my_cursor.execute(my_sql)
my_cursor.execute("SHOW TABLES")
