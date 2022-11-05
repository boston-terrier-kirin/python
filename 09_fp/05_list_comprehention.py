numbers = [1, 2, 3, 4, 5]

my_list = [num * 2 for num in numbers]
print(my_list)

my_list2 = [num * 2 for num in numbers if num % 2 == 0]
print(my_list2)
