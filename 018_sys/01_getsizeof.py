import sys

# list comprehension
# これだと一回配列にもってしまう
list_comprehension = sys.getsizeof([x * 10 for x in range(0, 10001)])

# generator
# generatorだと都度都度になるので、メモリ効率が良い
generator_exp = sys.getsizeof(x * 10 for x in range(0, 10001))

print(f"{list_comprehension} bytes")
print(f"{generator_exp} bytes")
