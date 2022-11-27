evens = [2, 4, 6]
odds = [1, 3, 5]

# +
numbers = evens + odds
print(numbers)

# - はできない
# print(numbers - odds)

# *
print(numbers * 2)

# in
list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

if "a" in list_1:
    print("aあり")

# ==, is
list_2 = []
list_2.append("a")
list_2.append("b")
list_2.append("c")

# == は、配列の中身をチェックする
print("==", list_1 == list_2)

# idで比較する場合はisを使う
print("is", list_1 is list_2)

list_3 = list_2
print("is", list_2 is list_3)