list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [10, 20, 30, 40, 50, 60]

result = zip(list_1, list_2)
my_list = list(result)
print(my_list)

# 残念ながらこれは上手くいかない
my_dict = dict(result)
print(my_dict)
print("*************************************")

# tuple unpackingと組み合わせて使う
days = ["Mon", "Tue", "Wed"]
fruits = ["Apple", "Banana", "Orange"]
drinks = ["Coffe", "Tea", "Beer"]

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)