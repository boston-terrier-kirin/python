user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 20
}

for item in user:
    print(item)
print("***************")

for item in user.items():
    # tuple unpacking
    key, value = item
    print(key, value)
print("***************")

# tuple unpacking
for key, value in user.items():
    print(key, value)
print("***************")

for value in user.values():
    print(value)
print("***************")

for key in user.keys():
    print(key)