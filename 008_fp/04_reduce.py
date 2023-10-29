from functools import reduce

numbers = [1, 2, 3, 4, 5]

##　関数バージョン
def sum(acc, item):
    return acc + item


result = reduce(sum, numbers, 0)
print(result)
print("***************")

## lambdaバージョン
result = reduce(lambda acc, item: acc + item, numbers, 0)
print(result)
print("***************")