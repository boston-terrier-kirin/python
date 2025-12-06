list_1 = [["a", "aa"], "b", "c"]

# 配列のコピーはこれ
list_2 = list_1[:]

# 違うアドレスになる
print(id(list_1), id(list_2))

# 違うアドレスにはなるが、shallow copyになっているので、list_2の変更は、list_1にも反映される
list_2[0][1] = "xx"
print(list_1, list_2)
print("***************")

# これだと同じアドレスになってしまう
list_3 = list_1
list_3[0] = "aa"

print(list_3, list_1)
print(id(list_3), id(list_1))
print("***************")
