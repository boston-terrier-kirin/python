# list自体がキーワードになっている
print(list)

# 変数名にlistが使えないわけではない
list = [1, 2, 3]
print(list)
print(len(list))
print("***************")

# listとarrayは違うらしい
list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

# slice
print(list_1[1:])
print(list_1[-1])
print("***************")

list_2 = []
list_2.append("a")
list_2.append("b")
list_2.append("c")

# insert
list_1.insert(1, "aa")
print("insert", list_1)
print("***************")

# insertは先頭に追加していく場合に使える
list_1.insert(0, "xx")
list_1.insert(0, "yy")
list_1.insert(0, "zz")
print("insert", list_1)