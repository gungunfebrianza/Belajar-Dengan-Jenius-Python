class Person:
    def __init__(self, firstname, lastname, age, eyecolor):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.eyecolor = eyecolor

    def getFullName(self):
        print(self.firstname + " " + self.lastname)
        # return self.firstname + " " + self.lastname


class Agent(Person):
    def __init__(self, division, firstname, lastname, age, eyecolor):
        super().__init__(firstname, lastname, age, eyecolor)
        self.division = division

    def sayhello(self):
        Person.getFullName(self)


CIA = Agent("National Security", "Gun Gun", "Febrianza", 28, "Black")
print(CIA.sayhello())

