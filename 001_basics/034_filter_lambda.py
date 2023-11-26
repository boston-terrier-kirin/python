def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5]

# filterでループする
for item in filter(check_even, my_nums):
    print(item)

print("***************")

# filterした結果をlistにする
result = list(filter(check_even, my_nums))
print(result)
print("***************")

# lambda
result = list(filter(lambda num: num % 2 == 0, my_nums))
print(result)
print("***************")
