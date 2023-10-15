# list unpacking
result = [1, 2, 3, 4, 5, 6]

a, b, *others = result

print(a)
print(b)
print(others)
print("*************************************")

# formatへのパラメータにもできる
points = [1140, -1140, 0]

mail_body = """決済総額: {0}
ポイント/キャッシュ利用: {1}
お支払金額: {2}
""".format(*points)

# * は、list unpacking。こういう時にも使える
print(mail_body)
print("*************************************")

# * でjsの...相当もできる
list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

list_2 = []
list_2.append("あ")
list_2.append("い")
list_2.append("う")

list_3 = [*list_1, *list_2]
print(list_3)
print(len(list_3))