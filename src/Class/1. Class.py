# CREATE CLASS
class Person:
    def __init__(self, firstname, lastname, age, eyecolor):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.eyecolor = eyecolor

    def getFullName(self):
        print(self.firstname + " " + self.lastname)

# CREATE OBJECT
hooman = Person("Maudy", "Ayunda", 25, "Brown")

# ACCESS PROPERTIES
print(hooman.age)  # 25

# ACCESS METHODS
hooman.getFullName()  # Maudy Ayunda

# CHANGE PROPERTIES
hooman.lastname = "Ayunda Faza"
hooman.getFullName()  # Maudy Ayunda Faza

# DELETE PROPERTIES
# del hooman.age

# DELETE OBJECTS
# del hooman