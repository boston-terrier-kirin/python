##　関数バージョン
def multiply(item):
    return item * 2


result = map(multiply, [1, 2, 3])
print(result)

# ここで初めて実行される
my_list = list(result)
print(my_list)
print("***************")

## lambdaバージョン
result = map(lambda item: item * 2, [1, 2, 3])
print(result)

# ここで初めて実行される
my_list = list(result)
print(my_list)
