import json

lover = '{"Name":"Maudy", "Age":24}'

jsonvar = json.loads(lover)

print(jsonvar["Name"])  # Maudy
print(jsonvar["Age"])  # 24
