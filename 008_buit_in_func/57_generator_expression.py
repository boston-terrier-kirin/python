numbers = [1, 2, 3, 4, 5]

print("> generator expression")
my_list = (num * 2 for num in numbers)
print(my_list)

# list comprehensionとは違って、generatorになっている
for x in my_list:
    print(x)
print("*****")

# generatorなので、2回目は何も表示されない。
for x in my_list:
    print(x)
