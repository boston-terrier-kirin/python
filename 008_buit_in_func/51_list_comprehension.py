numbers = [1, 2, 3, 4, 5]

print("> list comprehension")
my_list = [num * 2 for num in numbers]
print(my_list)
print("")

print("> map")
my_list = list(map(lambda num: num * 2, numbers))
print(my_list)
print("")

print("> list comprehension conditional")
my_list2 = [num * 2 for num in numbers if num % 2 == 0]
print(my_list2)
print("")

print("> filter + map")
# step_1 = filter(lambda num: num % 2 == 0, numbers)
# step_2 = map(lambda num: num * 2, step_1)
# my_list2 = list(step_2)
# ↓
my_list2 = list(map(lambda num: num * 2, filter(lambda num: num % 2 == 0, numbers)))
print(my_list2)
print("")

print("> str")
my_list3 = [l for l in "Kuroro"]
print(my_list3)
print("")

my_list4 = "".join(char for char in "Kuroro" if char not in "aiueo")
print(my_list4)
