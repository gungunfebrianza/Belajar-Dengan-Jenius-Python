# CREATE TUPPLE
animal = ("Boar", "Anoa", "Eagle", "Eagle")
print(animal)
print(type(animal))  # <class 'tuple'>

# LIST DATA TYPES
tupplestring = ("Indonesia", "Japan", "South Korea", "Thailand")
tupplestringinteger = (44, 55, 66, 77, 88, 99)
tupplestringboolean = (True, False, True, False)
tupplestringheterogen = ("Avenger", 99, False)

# ACCESS TUPPLES
print(animal[1])  # Anoa
print(animal[-1])  # Eagle
print(animal[0:2])  # ('Boar', 'Anoa')
print(type(animal[0:2]))  # <class 'tuple'>
print(animal[0:])  # ('Boar', 'Anoa', 'Eagle', 'Eagle')
print(animal[1:])  # ('Anoa', 'Eagle', 'Eagle')
print(animal[2:])  # ('Eagle', 'Eagle')
print(animal[3:])  # ('Eagle',)
print(animal[4:])  # ()
print(animal[52:])  # ()
print(animal[:0])  # ()
print(animal[:1])  # ('Boar',)
print(animal[:2])  # ('Boar', 'Anoa')
print(animal[:3])  # ('Boar', 'Anoa', 'Eagle')

# COUNT TUPPLE
print(len(animal))  # 4

