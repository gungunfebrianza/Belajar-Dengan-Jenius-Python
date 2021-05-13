import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test",
)

my_cursor = my_database.cursor()

# PULL DATA FROM THE TABLE
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
    print(row[0] + "\t%s" % row[1] + "\t\t%s" % row[2] + "\t%s" % row[3])

# DELETE RECORDS
my_sql = "DELETE FROM users WHERE name  = 'John'"
my_cursor.execute(my_sql)
my_database.commit()

# PULL DATA FROM THE TABLE
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
    print(row[0] + "\t%s" % row[1] + "\t\t%s" % row[2] + "\t%s" % row[3])
