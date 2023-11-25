def get_unlimited_multiples(num=1):
    current = num

    while True:
        yield current
        current += num


sevens = get_unlimited_multiples(7)
print(next(sevens))
print(next(sevens))
print(next(sevens))
print(next(sevens))
