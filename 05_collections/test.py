# https://docs.python.org/3.11/library/collections.html
from collections import Counter, defaultdict, OrderedDict

list = [1, 2, 3, 4, 5, 5, 5]
print(Counter(list))

words = "Yes, We Can."
print(Counter(words))
print("***************")

# 存在しないキーを指定するとエラーになってしまうのを、defaultdictで初期値を設定できる。
dic = defaultdict(lambda: "N/A", {"a": 1, "b": 2})
print("a", dic["a"])
print("c", dic["c"])
print("***************")

# 通常のDictionary
ndic_1 = {}
ndic_1["a"] = 1
ndic_1["b"] = 2
ndic_1["c"] = 3

ndic_2 = {}
ndic_2["a"] = 1
ndic_2["c"] = 3 # ココ
ndic_2["b"] = 2

# pythonでは意外なことにTrueになる。
print("Dictionary", ndic_1 == ndic_2)

# OrderedDict
odic_1 = OrderedDict()
odic_1["a"] = 1
odic_1["b"] = 2
odic_1["c"] = 3

odic_2 = OrderedDict()
odic_2["a"] = 1
odic_2["c"] = 3 # ココ
odic_2["b"] = 2

# OrderedDictは、順番まで見て判定する。
print("OrderedDict", odic_1 == odic_2)