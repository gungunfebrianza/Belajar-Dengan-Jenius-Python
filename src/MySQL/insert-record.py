import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test",
)

# print(my_database)

my_cursor = my_database.cursor()

# INSERT ONE RECORD
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)
my_cursor.execute(sqlStuff, record1)
my_database.commit()

# INSERT MULTIPLE RECORDS
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Tim", "tim@tim.com", 32), ("Mary", "Mary@mary.com", 21),
           ("Steve", "steve@steveEmail.com", 57),
           ("Tina", "tina@somethingellse.com", 29), ]
my_cursor.executemany(sqlStuff, records)
my_database.commit()
