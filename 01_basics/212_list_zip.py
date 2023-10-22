names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

print(zip(names, ages))
print("=============================")

for name, age in zip(names, ages):
    print(name, age)

print("=============================")

print(list(zip(names, ages)))
