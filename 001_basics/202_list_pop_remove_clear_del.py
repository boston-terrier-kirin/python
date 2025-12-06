list_1 = ["a", "b", "c"]

## popは元の配列をmutateする
# 一番後ろから削除。後ろから順に削除しながら処理する場合に使える
while len(list_1) > 0:
    # popした値はreturnされる
    print("pop", list_1.pop())

# list_1は空になっている
print(list_1)
print("***************")

## pop(index)
list_1 = ["a", "b", "c"]

# index指定でpopできる
list_1.pop(1)
print(list_1)
print("***************")

## remove
list_2 = ["a", "b", "c", "a", "a"]

print(list_2)

# aが全部消えるわけではなく、最初に見つかったaが消えている
list_2.remove("a")
print("remove", list_2)
print("***************")

## clear
list_2.clear()
print("clear", list_2)

## del
list_3 = ["a", "b", "c", "d", "e"]
del list_3[0:2]
print("del", list_3)
