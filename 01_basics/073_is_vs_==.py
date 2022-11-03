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