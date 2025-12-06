list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

# insert
list_1.insert(1, "aa")
print("insert", list_1)
print("***************")

# insertは先頭に追加していく場合に使える
list_1.insert(0, "xx")
list_1.insert(0, "yy")
list_1.insert(0, "zz")
print("insert", list_1)
