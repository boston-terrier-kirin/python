def my_decorator(fn):
    def wrap_fn():
        print("*****")
        fn()
        print("*****")

    return wrap_fn


@my_decorator
def hello():
    print("Hello")


hello()

# @my_decorator でやっていることはこれと同じ
def hello2():
    print("Hello")

my_decorator(hello2)()
