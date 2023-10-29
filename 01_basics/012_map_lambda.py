def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

# mapでループする
for item in map(square, my_nums):
    print(item)

print("***************")

# mapした結果をlistにする
result = list(map(square, my_nums))
print(result)
print("***************")

# lambda
result = list(map(lambda num: num**2, my_nums))
print(result)
print("***************")
