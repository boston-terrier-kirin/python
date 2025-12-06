nums = [0] * 10

print(nums)

print("=" * 10)

# これは要注意。作られた配列は同じidになってしまう。
row = [0, 0, 0]
matrix = [row] * 3
print(matrix)

print(id(matrix[0]), id(matrix[1]), id(matrix[2]))

# 3つの配列に値が反映されてしまう
matrix[0][0] = 100
print(matrix)
