s = "gnu's not linux"

print(s.index("n"))
print(s.index("n", 2))
print("*" * 10)

# 意外なことに見つからないと、ValueError: substring not foundになる。
# print(s.index("n", 13))

# findを使えば、見つからない場合に -1 が返ってくる。
print(s.find("n"))
print(s.index("n", 2))
print(s.find("n", 13))
print("*" * 10)

# indexはlistに対しても使える。
data = [1, 2, 3, 4]
print(data.index(3))
