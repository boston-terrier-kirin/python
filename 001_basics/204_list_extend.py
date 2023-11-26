# extendは、list_1自体がmutateされる
list_1 = ["a", "b", "c"]

list_2 = ["あ", "い", "う"]

list_1.extend(list_2)
print(list_1)
