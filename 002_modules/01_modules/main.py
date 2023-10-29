# 関数を指定してimport
from shopping.cart import buy
# モジュールを指定してimport
from util import util

# 標準モジュール
import random as rand
import sys

result = buy("laptop pc")

print(result)

print(util.multiply(2, 5))
print(util.divide(12, 3))
print("***************")

# random
print(rand.random())
print(rand.randint(1, 10))
print(rand.choice([1, 4, 7, 8, 9]))

my_list = [1, 4, 7, 8, 9]
rand.shuffle(my_list)
print(my_list)
print("***************")

# sys
args = sys.argv
print(args[1:])