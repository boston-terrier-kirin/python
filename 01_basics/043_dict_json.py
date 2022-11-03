import json

# json -> dict
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'
user = json.loads(userJSON)
for key, value in user.items():
    print(key, value)
print("*************************************")

# dict -> json
car = {"make": "Toyota", "model": "CHR", "year": 2022}
carJSON = json.dumps(car)
print(carJSON)
