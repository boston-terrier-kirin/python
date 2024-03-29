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
# jsの、myMap.get("c") || "" ができる
print(myDic.get("c", ""))
print("***************")

# in
print("a" in myDic)
print("c" in myDic)
print("***************")

# copy
myDic2 = myDic.copy()
myDic2["c"] = 3
print(myDic, myDic2)
print("***************")

# update
user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 20
}
user.update({"age": 55})
print("update", user)
print("***************")

# updateというか、mergeに近いことができる
user_attr = {
    "address": "Boston, MA",
    "hobby": " Basketball"
}

user.update(user_attr)
print("update", user)
print("***************")

# popでキーを消す
user.pop("age")
print("pop", user)
print("***************")

# updateはキーが存在しない場合でも使える
user.update({"age": 57})
print("update", user)
print("***************")
