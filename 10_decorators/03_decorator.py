def my_decorator(fn):
    def wrap_fn(*args, **kwargs):
        print("*****")
        print(f"params: {args} {kwargs}")
        fn(*args, **kwargs)
        print("*****")

    return wrap_fn


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello("Hi", "💨")
