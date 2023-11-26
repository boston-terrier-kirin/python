# == は値で比較している
print("True == 1", True == 1)
print("'' == 0", "" == 0)
print("[] == 0", [] == 0)
print("10 == '10'", 10 == "10")
print("10 == 10.0", 10 == 10.0)
print("[1, 2, 3] == [1, 2, 3]", [1, 2, 3] == [1, 2, 3])
print("***************")

# is はポインターで比較する
print("True is True", True is True)
print("'a' is 'a'", "a" is "a")
print("10 is 10", 10 is 10)
print("'' is 0", "" is 0)
print("[] is 0", [] is 0)
print("10 is '10'", 10 is "10")
print("10 is 10.0", 10 is 10.0)
print("[1, 2, 3] is [1, 2, 3]", [1, 2, 3] is [1, 2, 3])
print("***************")

# 意外にもTrue, shared referenceが効く
value_1 = "Apple"
value_2 = "Apple"
print(value_1 is value_2)

# idは同じになっている
print(id(value_1), id(value_2))