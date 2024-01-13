s = "gnu's not linux"
print(list(enumerate(s)))

print(s.index("n"))
print(s.index("n", 2))

# 意外なことに見つからないと、ValueError: substring not foundになる
# print(s.index("n", 13))
