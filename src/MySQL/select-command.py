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

# WHERE CLAUSE
my_cursor.execute("SELECT * FROM users WHERE name =  'John'")
result = my_cursor.fetchall()
for row in result:
    print(row)

# WHERE and LIKE WILDCARDS
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%'")
result = my_cursor.fetchall()
for row in result:
    print(row)

# AND / OR Clause
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 29 AND user_id = 5")
result = my_cursor.fetchall()
for row in result:
    print(row)
