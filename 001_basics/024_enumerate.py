# list
for index, item in enumerate([1, 2, 3]):
    print(index, item)
print("***************")

word = "abcdefg"
for letter in enumerate(word):
    # tupleが返ってくる
    print(letter)

print("***************")
for letter in enumerate(word):
    print(letter[0], letter[1])

print("***************")
# tuple unpacking
for index, letter in enumerate(word):
    print(index, letter)