list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

list_2 = list_1

list_3 = []
list_3.append("a")
list_3.append("b")
list_3.append("c")

# idで実態がわかる
print(id(list_1), id(list_2), id(list_3))

