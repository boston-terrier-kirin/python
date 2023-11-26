def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt

        cnt = cnt + 1
        print(f"{fn.__name__} has been called {cnt} times")

        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


c1 = counter(add)
c1(10, 20)
c1(10, 30)

c2 = counter(sum)
result = c2([10, 20, 30, 40])
print(result)
