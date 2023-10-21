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
list_1 = ["a", "b", "c"]
list_2 = ["あ", "い", "う"]

list_3 = [*list_1, *list_2]
print(list_3)
print(len(list_3))
print("*************************************")

# concatでも...相当ができる
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
print(list_a + list_b)
