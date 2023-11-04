numbers = [1, 2, 3, 4, 5, 2, 4]

# list
my_list = [num * 2 for num in numbers]
print(my_list)

my_list2 = [num * 2 for num in numbers if num % 2 == 0]
print(my_list2)
print("***************")

# setの場合は、重複が削除される
my_set = {num * 2 for num in numbers}
print(my_set)

my_set2 = {num * 2 for num in numbers if num % 2 == 0}
print(my_set2)
