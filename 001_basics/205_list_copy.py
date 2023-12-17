list_1 = ["a", "b", "c"]

# 配列のコピーはこれ
list_2 = list_1[:]

# 違うアドレスになる
print(id(list_1), id(list_2))

list_2[0] = "xx"
print(list_1, list_2)
print("***************")

# これだと同じアドレスになってしまう
list_3 = list_1
list_3[0] = "aa"

print(list_3, list_1)
print(id(list_3), id(list_1))
print("***************")