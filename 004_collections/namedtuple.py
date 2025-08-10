from collections import namedtuple

Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="sammy")

print(sammy)

# attrでもindexでも呼べるようになる
# Husky
print(sammy.breed)

# age=5
print(sammy[0])

# tuple unpacking
age, breed, name = sammy
print(age, breed, name)
