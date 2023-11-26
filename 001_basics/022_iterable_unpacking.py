# list unpacking
a, b, c = [1, 3, 5]
print(a, b, c)

# これはtuple
a = 10, 20
print(type(a))

# これはパラレルアサインというよりは
a, b = 10, 20
# ↓ と同じ意味なので、実際はtuple unpacking
a, b = (10, 20)
print(a, b)

# pythonはtmpを使わずにswapできる
value_1 = 100
value_2 = 567
value_1, value_2 = value_2, value_1
print(value_1, value_2)

# setは順番が保証されていないので役には立たないが、unpackingはできる
s = {"p", "y", "t", "h", "o", "n"}
a, b, c, d, e, f = s
print(a, b, c, d, e, f)

# dictはキーがunpackingされる
d = {"aa": 100, "bb": 200, "cc": 567}
a, b, c = d
print(a, b, c)

# 値のunpacking
a, b, c = d.values()
print(a, b, c)

# これはdictのunpacking
for k, v in d.items():
    print(k, v)
