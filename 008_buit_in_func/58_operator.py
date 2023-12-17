import operator
from functools import reduce

# lambdaの場合
result = reduce(lambda acc, v: acc + v, [1, 2, 3, 4])
print(result)

# operatorの場合
result = reduce(operator.add, [1, 2, 3, 4])
print(result)
