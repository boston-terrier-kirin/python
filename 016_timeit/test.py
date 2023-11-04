import timeit

# timeでも性能は取れるが、timeitの方が正確に取れるらしい。

# 性能1
stmt = """
func_one(100)
"""
setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""
result = timeit.timeit(stmt, setup, number=10000)
print(result)

# 性能2
stmt = """
func_two(100)
"""
setup = """
def func_two(n):
    return list(map(str, range(n)))
"""
result = timeit.timeit(stmt, setup, number=10000)
print(result)