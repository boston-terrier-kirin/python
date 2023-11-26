def my_for(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
            func(item)
        except StopIteration:
            break


def square(x):
    print(x * x)


my_for("hello", print)
print("*****")
my_for([1, 2, 3, 4, 5], square)
