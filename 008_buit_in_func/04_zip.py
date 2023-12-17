list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [10, 20, 30, 40, 50, 60]

result = zip(list_1, list_2)
my_list = list(result)
print(my_list)

# 残念ながらこれは上手くいかない -> zipはgeneratorを返すので2回目はなにも表示されない。zipを作り直せばdictに変換できる
result = zip(list_1, list_2)
my_dict = dict(result)
print(my_dict)
print("*************************************")

# tuple unpackingと組み合わせて使う
days = ["Mon", "Tue", "Wed"]
fruits = ["Apple", "Banana", "Orange"]
drinks = ["Coffe", "Tea", "Beer"]

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dict comprehensionと組み合わせて使う
students = ["dan", "ang", "kate"]
midterms = [80, 91, 78]
finals = [98, 89, 53]

# {'dan': 98, 'ang': 91, 'kate': 78}
students_grade = {grade[0]: max(grade[1], grade[2]) for grade in zip(students, midterms, finals)}
print(students_grade)

# mapでもできる
students_grade = zip(students,
                     map(lambda pairs: max(pairs), zip(midterms, finals)))
print(dict(students_grade))

# zipはdictに変換できる
dogs = ["kirin", "kuroro"]
ages = [15, 3]
dogs_ages = dict(zip(dogs, ages))
print(dogs_ages)
