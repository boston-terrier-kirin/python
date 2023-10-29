def create_cubes(n):
    for x in range(n):
        yield x ** 3


# これでresultSetを1行づつ処理するような感じにできる
for value in create_cubes(10):
    print(value)
print("********************")

# listにキャストすることも可能
print(list(create_cubes(10)))
print("********************")

# nextで呼び出すこともできる
g = create_cubes(10)
print(next(g))
print(next(g))
print(next(g))
