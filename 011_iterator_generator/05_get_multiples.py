def get_multiples(num=1, count=10):
    current = 1
    next_num = num
    while current <= count:
        yield next_num
        next_num += num
        current += 1


print(list(get_multiples(2, 3)))
