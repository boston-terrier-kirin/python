# extendは、[...list_1, ...list_2] 相当
list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

list_2 = []
list_2.append("あ")
list_2.append("い")
list_2.append("う")

list_1.extend(list_2)
print(list_1)