# CREATE LIST
animal = ['Snake', 'Wolf', 'Monkey', 'Tiger', 'Tiger']

# ACCESS ITEMS
print(animal[0])
print(animal[-1])  # Negative Indexing
print(type(animal[-1]))  # <class 'str'>
print(animal[1:3])  # Range of Indexes
print(type(animal[1:3]))  # <class 'list'>
print(animal[2:])  # ['Monkey', 'Tiger', 'Tiger']
print(animal[:3])  # ['Snake', 'Wolf', 'Monkey']

print(animal.count('Tiger'))  # 2
print(animal.index('Snake'))  # 0
print(animal.index('Wolf'))  # 1
print(len(animal))  # 5
print(type(animal))  # <class 'list'>
print(animal)

# LIST DATA TYPES
liststring = ["Indonesia", "Japan", "South Korea", "Thailand"]
listinteger = [44, 55, 66, 77, 88, 99]
listboolean = [True, False, True, False]
listheterogen = ["Avenger", 99, False]


