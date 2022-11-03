my_set = {1, 2, 3, 4, 5, 5}

my_set.add(6)
my_set.add(6)
print(my_set)
print("***************")

my_set.remove(3)
print(my_set)
print("***************")

# キー存在チェック
if 1 in my_set:
    print("1あり")
print("***************")

# 重複削除
my_list = [1, 2, 3, 4, 4, 5, 5, 3]
unique = set(my_list)
print(unique)
print("***************")

# これはできない
# TypeError: 'set' object is not subscriptable
# print(my_set[2])
# indexを使いたい場合は、listにcastすればOK
print(list(my_set)[2])
print("***************")

# これはできる
for item in my_set:
    print(item)