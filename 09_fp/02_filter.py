##　関数バージョン
def even(item):
    return item % 2 == 0


result = filter(even, [1, 2, 3, 4, 5, 6])
even_list = list(result)
print(even_list)
print("***************")

## lambdaバージョン
result = filter(lambda item: item % 2 == 0, [1, 2, 3, 4, 5, 6, 8, 6, 8])
even_list = list(result)
print(even_list)
print("***************")

# setに変換すると順番が保証されなくなる
even_list = set(even_list)
print(even_list)