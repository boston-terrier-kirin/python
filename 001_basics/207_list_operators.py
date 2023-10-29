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
list_1 = ["a", "b", "c"]

if "a" in list_1:
    print("aあり")

# ==, is
list_2 = ["a", "b", "c"]

# == は、配列の中身をチェックする
print("==", list_1 == list_2)

# idで比較する場合はisを使う
print("is", list_1 is list_2)

list_3 = list_2
print("is", list_2 is list_3)