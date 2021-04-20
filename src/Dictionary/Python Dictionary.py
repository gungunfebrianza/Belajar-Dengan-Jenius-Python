
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


print(len(dictionarymaudy))  # 3

