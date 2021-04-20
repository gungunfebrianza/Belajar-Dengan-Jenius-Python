
# CREATION
dictionarymaudy = {
    "Name":"Maudy",
    "Age":24,
    "Profession":"Singer",
    "Songs": ["Perahu Kertas", "By My Side", "Untuk Apa"]
}

print(dictionarymaudy)  # {'Name': 'Maudy', 'Age': 24, 'Profession': 'Singer'}


# ACCESS ITEM
print(dictionarymaudy.get("Name"))  # Maudy
print(dictionarymaudy["Age"])  # 24
print(dictionarymaudy.get("SONGS"))  # None
print(dictionarymaudy.keys())  # dict_keys(['Name', 'Age', 'Profession', 'Songs'])
print(dictionarymaudy.values())  # dict_values(['Maudy', 24, 'Singer', ['Perahu Kertas', 'By My Side', 'Untuk Apa']])
dictionarymaudy["Profession"] = "Actrees"
print(dictionarymaudy.get("Profession"))  # Actrees
dictionarymaudy.update({"Profession":"Aspirator"})
dictionarymaudy.update({"Status":"Single"})
dictionarymaudy.update({"KeyExample":"ValueExample"})
# dictionarymaudy.pop("KeyExample")
# dictionarymaudy.popitem()  # Remove The Last Inserted Item
# del dictionarymaudy["KeyExample"]
# del dictionarymaudy  # Delete Dictionary
print(dictionarymaudy.get("Profession"))  # Aspirator
print(dictionarymaudy.items())  # Return as tuples in a list
if "Songs" in dictionarymaudy:
    print("Songs Key Exist!")
# dictionarymaudy.clear()
print(dictionarymaudy)
print(len(dictionarymaudy))  # 5

# LOOPING
for x in dictionarymaudy:
    print(x)
    print(dictionarymaudy[x])

for x in dictionarymaudy.keys():
    print(x)

for x in dictionarymaudy.values():
    print(x)

for x, y in dictionarymaudy.items():
    print(x,y)

#COPY

cloningvariable = dictionarymaudy.copy()
print(cloningvariable)