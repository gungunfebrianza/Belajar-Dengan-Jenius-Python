import json

lover = '{"Name":"Maudy", "Age":24}'

jsonvar = json.loads(lover)

print(jsonvar["Name"])  # Maudy
print(jsonvar["Age"])  # 24

dictionaryprocessor = {"Type": "Intel i7", "Generation":"10th"}  # Python Object Dictionary

jsonstring = json.dumps(dictionaryprocessor)

print(jsonstring)  # {"Type": "Intel i7", "Generation": "10th"}
print(type(jsonstring))  # <class 'str'>
