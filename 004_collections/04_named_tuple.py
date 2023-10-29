from collections import  namedtuple

Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="sammy")

print(sammy)

# attrでもindexでも呼べるようになる
print(sammy.breed)
print(sammy[1])
