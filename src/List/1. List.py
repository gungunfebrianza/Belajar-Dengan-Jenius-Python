# CREATE LIST
animal = ['Snake', 'Wolf', 'Monkey', 'Tiger', 'Tiger']
print(animal)
print(type(animal))  # <class 'list'>

# LIST DATA TYPES
liststring = ["Indonesia", "Japan", "South Korea", "Thailand"]
listinteger = [44, 55, 66, 77, 88, 99]
listboolean = [True, False, True, False]
listheterogen = ["Avenger", 99, False]

# ACCESS ITEMS
print(animal[0])
print(animal[-1])  # Negative Indexing
print(type(animal[-1]))  # <class 'str'>
print(animal[1:3])  # Range of Indexes
print(type(animal[1:3]))  # <class 'list'>
print(animal[2:])  # ['Monkey', 'Tiger', 'Tiger']
print(animal[:3])  # ['Snake', 'Wolf', 'Monkey']

# CHANGE ITEMS
animal[0] = "Bear"
print(animal[0])  # Bear
animal[1:2] = ["Bull", "Eagle"]
print(animal)  # ['Bear', 'Bull', 'Eagle', 'Monkey', 'Tiger', 'Tiger']

# INSERT ITEMS
animal.insert(0, "Shark")  # Insert at specific Index without replace
print(animal[0:2])  # ['Shark', 'Bear']
animal.append("Dolphins")  # Add Item to the end of list
print(animal[5:])  # ['Tiger', 'Tiger', 'Dolphins']
insect = ["Mosquito", "Dragon Fly", "Butterfly"]
animal.extend(insect)
print(animal)

# COUNT LIST
print(animal.count('Tiger'))  # 2
print(animal.index('Bear'))  # 1
print(animal.index('Bull'))  # 2
print(len(animal))  # 11

# FIND LIST
if "Avenger" in listheterogen:
    print("Avenger is Exist!")

# REMOVE ITEMS
animal.remove("Dolphins")
print(animal)
animal.pop(-2)  # Remove at specific index
print(animal)
animal.pop()  # Remove the last Item
print(animal)
del animal[0]
print(animal)

# DELETE LIST
# del animal

# CLEAR LIST
# animal.clear()


# LOOPING LIST
for x in liststring:
    print(x)

for i in range(len(listheterogen)):
    print(listheterogen[i])

i = 0
while i < len(listinteger):
    print(listinteger[i])
    i = i + 1

# LIST COMPREHENSION
[print(x) for x in listheterogen]

listcat = [x for x in animal if "Tiger" in x]
print(listcat)  # ['Tiger', 'Tiger']
listnoncat = [x for x in animal if x != "Tiger"]
print(listnoncat)

# SORT LIST
print(animal)  # Before Sort
animal.sort()
print(animal)  # After Sort

