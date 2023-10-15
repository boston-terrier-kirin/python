# tupleは変更できない
itabashi = (35.762406, 139.700026)

print(itabashi[0])
print(itabashi[1])

user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 20
}

# dict.itemsで戻ってくるのはtuple
# dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 20)])
print(user.items())