list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

print(len(list_1))
print("***************")

list_1.insert(1, "aa")
print(list_1)
print("***************")

# 一番後ろから削除
list_1.pop()
print(list_1)
print("***************")

# aaが全部消えるわけではなく、最初に見つかったaaが消えている
list_1.append("aa")
print(list_1)
list_1.remove("aa")
print(list_1)
print("***************")

list_1.clear()
print("clear", list_1)