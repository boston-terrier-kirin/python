# mutableをデフォルト値にする場合は注意が必要
def add_item(name, quantity, unit, grocery_list=[]):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list


store1 = add_item("banana", 2, "units")
add_item("milk", 1, "liter", store1)
print(store1)

store2 = add_item("python", 1, "medium-rare")
print(store2)

# デフォルト値はモジュールが呼ばれ時に評価されるので、store1とstore2は同じアドレスになっている。
print(id(store1), id(store2))
