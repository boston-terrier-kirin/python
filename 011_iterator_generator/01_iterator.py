nums = [1, 2, 3, 4, 5]

# listはiteratorではなくて、iterable
# TypeError: 'list' object is not an iterator
# next(nums)

# iterableに対して、iterすると、iteratorをGETできる
it = iter(nums)
print(it)

# iteratorはnextを呼ぶと値を返す
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# StopIterationになるまで値を返す
# print(next(it))

# これはiter(num)をやって、nextしている
for num in nums:
    print(num)
