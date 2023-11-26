def averager():
    total = 0
    count = 0

    def add(number):
        # nonlocalにしないとtotal/countが解決できない
        # UnboundLocalError: local variable 'total' referenced before assignment
        nonlocal total
        nonlocal count

        total = total + number
        count = count + 1
        return total / count

    return add


a = averager()
print(a(10))
print(a(20))
print(a(30))

print(b.__closure__)
