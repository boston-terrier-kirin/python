# == は値で比較している模様
print(True == 1)
print("" == 0)
print([] == 0)
print(10 == "10")
print(10 == 10.0)
print([1,2,3] == [1,2,3])
print("***************")

# is はポインターで比較する
print(True is True)
print("a" is "a")
print(10 is 10)
print("" is 0)
print([] is 0)
print(10 is "10")
print(10 is 10.0)
print([1,2,3] is [1,2,3])

# 意外にもTrue
value_1 = "Apple"
value_2 = "Apple"
print(value_1 is value_2)

# stringキャッシュが効くのか、idは同じになっている
print(id(value_1), id(value_2))