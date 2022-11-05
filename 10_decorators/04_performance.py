from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()

        print(f"it took: {end - start} sec")

        return result

    return wrapper


@performance
def test(repeat):
    for i in range(repeat):
        i ** 2

    return i


print(test(10000000))
