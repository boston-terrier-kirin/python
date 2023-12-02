names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

print(zip(names, ages))
print("=============================")

for name, age in zip(names, ages):
    print(name, age)

print("=============================")

print(list(zip(names, ages)))
print("=============================")

# dictに変換
person_dict = [{person[0]: person[1]} for person in zip(names, ages)]
for person in person_dict:
    print(person)