## 関数バージョン
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

# ここで初めて実行されるの意味は、↓
my_list = list(result)
print(my_list)


## python3のmapはgeneratorを返す
def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


results = map(fact, range(6))

for x in results:
    print(x)
print("*****")

# python3のmapはgeneratorを返すので、2回目は何も表示されない。
# list comprehensionはlistを作ってしまうが、mapはGeneratorを返すので、性能面で有利ではある。
# というわけで、generator expressionが登場する。
for x in results:
    print(x)
