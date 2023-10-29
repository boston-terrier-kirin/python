from collections import defaultdict

dic = {
    "a": 10,
    "b": 20
}

# dictはキーがないとエラーになる。
try:
    print(dic["c"])
except KeyError as err:
    print("Error", err)

# defaultdictはデフォルト値をセットできる
d_dic = defaultdict(lambda: "0", dic)
print(d_dic["c"])
