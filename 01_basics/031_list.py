# list自体がキーワードになっている
print(list)

# 変数名にlistが使えないわけではない
list = [1, 2, 3]
print(list)

# listとarrayは違うらしい
list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

print(list_1)
print(list_1[1:])
print(list_1[-1])
print("***************")

for item in list_1:
    print(item)
print("***************")

list_2 = []
list_2.append("a")
list_2.append("b")
list_2.append("c")

# 意外にもこれはTrue
print(list_1 == list_2)
print("***************")

# これだと同じPointerになってしまう
list_3 = list_2
list_3[0] = "aa"

print(list_2, list_3)
print("***************")