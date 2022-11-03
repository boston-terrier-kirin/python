name = "kohei matsumoto"

# jsのsplitとはちょっと違う
print(name.split(" "))
print(name.split())

# これはできない
# ValueError: empty separator
# print(name.split(""))

# これはできる
print(list(name))

# str自体が最初からiterableなので、1文字づつ処理したい場合はforを使う
for letter in name:
    print(letter)