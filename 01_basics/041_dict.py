# dict自体がキーワードになっている
print(dict)

myDic = {}
myDic["a"] = 1
myDic["b"] = 2

# 上書きできる
myDic["b"] = 3

print(myDic)
print(myDic["a"])
print(myDic.get("b"))
print("***************")

# getだとエラーにならず、Noneが返ってくる
print(myDic.get("c"))
print("***************")

# デフォルトも設定できる
print(myDic.get("c", ""))
print("***************")

# in
print("a" in myDic)
print("c" in myDic)
print("***************")

# ループ
for key in myDic:
    print(key, myDic.get(key))
print("***************")

# copy
myDic2 = myDic.copy()
myDic2["c"] = 3
print(myDic, myDic2)

user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 20
}

# update
user.update({"age": 55})
print(user)
print("***************")

# popでキーを消す
user.pop("age")
print(user)
print("***************")

# updateはキーが存在しない場合でも使える
user.update({"age": 57})
print(user)

