list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

# pop
# 一番後ろから削除。後ろから順に削除しながら処理する場合に使える
while len(list_1) > 0:
    # popした値はreturnされる
    print("pop", list_1.pop())

print(list_1)
print("***************")

# pop(index)
list_1 = []
list_1.append("a")
list_1.append("b")
list_1.append("c")

# index指定でpopできる
list_1.pop(1)
print(list_1)
print("***************")

# remove
list_2 = []
list_2.append("a")
list_2.append("b")
list_2.append("c")
list_2.append("a")
list_2.append("a")

print(list_2)

# aが全部消えるわけではなく、最初に見つかったaが消えている
list_2.remove("a")
print("remove", list_2)
print("***************")

# clear
list_2.clear()
print("clear", list_2)