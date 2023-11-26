from functools import wraps


def counter(fn):
    cnt = 0

    # wrapsを使うと、helpした時にオリジナルのfnが表示される
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt

        cnt = cnt + 1

        # オリジナルのaddのidになる
        print(f"{fn.__name__} id={id(fn)} has been called {cnt} times")

        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


print(id(add))

add = counter(add)

# オリジナルのaddとは違うidになっている
print(id(add))

# でもできることは同じで、プラスアルファ。これがdecorator。
print(add(10, 20))
print(add(30, 40))


# @で書くとこうなる
@counter
def mult(a, b):
    return a * b


# wrapsを使うと、helpした時にオリジナルのfnが表示される
help(add)
help(mult)
