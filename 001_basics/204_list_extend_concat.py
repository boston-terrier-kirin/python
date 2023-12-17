# extendは、list_1自体がmutateされる
list_1 = ["a", "b", "c"]
print(id(list_1))

list_1.extend(["あ", "い", "う"])
print("*****")

print(list_1)
print(id(list_1))
print("*****")

# concatは新しいlistを作る
list_a = [1, 2, 3]
print(id(list_a))

list_a = list_a + ["a", "b", "c"]
print(id(list_a))
