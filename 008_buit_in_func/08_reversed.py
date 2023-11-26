# reversedはiterableを返す
for char in reversed("hello"):
    print(char)

# 文字列を逆にする
print("".join(list(reversed("hello"))))

# 文字列を逆にする
print("hello"[::-1])

# 逆順にループ
for x in reversed(range(0, 10)):
    print(x)
