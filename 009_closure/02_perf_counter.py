from time import perf_counter


def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start

    return poll


t = timer()
print(t())
print(t())
