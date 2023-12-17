import time


def time_it(fn, *arg, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        # unpackしている
        fn(*arg, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


ave_time = time_it(print, 1, 2, 3, sep=" - ", rep=5)
print(ave_time)
