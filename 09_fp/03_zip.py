list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [10, 20, 30, 40, 50, 60]

result = zip(list_1, list_2)
my_list = list(result)
print(my_list)

# 残念ながらこれは上手くいかない
my_dict = dict(result)
print(my_dict)
