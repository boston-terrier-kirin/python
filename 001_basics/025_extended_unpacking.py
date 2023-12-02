# stringのunpacking
s = "python"
a, *b = s
print(a, b)
print("*****")

a, *b, c = s
print(a, b, c)
print("*****")

# setはsliceができない、indexableではないので
# s = {1, 2, 3}
# a = s[0]
# b = s[1:]
# print(a, b)
s = {1, 2, 3}
a, *b = s
print(a, b)
print("*****")

# setにunpackすると、重複を削除できる
s1 = "abcc"
s2 = "ccde"
s = {*s1, *s2}
print(s)

# **はdictをunpacking
d1 = {"k1": 1, "k2": 2}
d2 = {"k2": 3, "k3": 4}

# これはkeyがsetにunpacking
ss = {*d1, *d2}
print(ss)

# **でdictのunpacking、重複するkeyの値は上書き
ss = {**d1, **d2}
print(ss)