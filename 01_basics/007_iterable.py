# list, dict, tuple, set, str

# list
for item in [1, 2, 3]:
    print(item)
print("***************")

# dict
for item in {"a": 1, "b": 2, "c": 3}.items():
    print(item)
print("***************")

# tuple
for item in (1, 2, 3):
    print(item)
print("***************")

# set
for item in {1, 2, 3}:
    print(item)
print("***************")

# str
for item in "string":
    print(item)
print("***************")

# break
for item in [1, 2, 3]:
    print(item)
    if item == 2:
        # breakできる
        break
print("***************")