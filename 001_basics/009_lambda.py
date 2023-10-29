# pep8 では普通の関数に変換されてしまう
# ここにコメントがあると、なぜか変換されない
getSum = lambda num1, num2 : num1 + num2

print(getSum(1, 2))
