# generatorは、
# (a) selectしたresultSetをまとめてListに入れてからreturnするのではなく
# (b) resultSetを1行づつ処理する
# ような感じと受け取った。(a)はListがメモリを食ってしまう。
def generator_fn():
    yield "Steph"
    yield "Clay"

# generatorはiterable
for item in generator_fn():
    print(item)
print("*****")

# もしくはこう使う
g = generator_fn();
print(next(g))
print(next(g))

# print(next(g)) -- 値がないとエラーになる