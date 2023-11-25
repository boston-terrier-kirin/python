# listの場合
l1 = [n for n in range(0, 10)]
print(l1)

# これでgeneratorが作れる
l2 = (n for n in range(0, 10))
print(l2)

# これだと1回配列を作ってからsumしている
sum1 = sum([n for n in range(0, 10)])
print(sum1)

# generatorを使えば配列を作らなくてもOKなので、メモリが少なくて済む
sum2 = sum(n for n in range(0, 10))
print(sum2)
