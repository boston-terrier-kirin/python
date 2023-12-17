from time_it import time_it


# ループバージョン
def compute_power_1(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n ** i)
    return results


results = compute_power_1(2, end=5)
print(results)
print("*****")


# list comprehensionバージョン
def compute_power_2(n, *, start=1, end):
    return [n ** i for i in range(start, end)]


results = compute_power_2(2, end=5)
print(results)
print("*****")


# generatorバージョン
def compute_power_3(n, *, start=1, end):
    return (n ** i for i in range(start, end))


results = compute_power_3(2, end=5)
print(list(results))
print("*****")


# time_it
results = time_it(compute_power_1, 2, start=0, end=10, rep=5)
print(results)
