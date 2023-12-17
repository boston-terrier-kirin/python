from functools import partial


def my_func(a, b, c):
    print(a, b, c)


# partialを使う場合
f = partial(my_func, a=10, b=20)
f(c=30)
f(a=100, c=30)

# lambdaを使う場合
f = lambda c: my_func(10, 20, c)
f(30)


# 関数でやる場合
def f(c):
    return my_func(10, 20, c)


f(30)
