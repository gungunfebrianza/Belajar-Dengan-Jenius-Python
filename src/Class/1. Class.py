class Person:
    def __init__(self, firstname, lastname, age, eyecolor):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.eyecolor = eyecolor

    def getFullName(self):
        print(self.firstname + " " + self.lastname)


hooman = Person("Maudy", "Ayunda", 25, "Brown")
hooman.getFullName()
