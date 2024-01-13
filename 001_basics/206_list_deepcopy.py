# copyはshallow copyになっている
l_original = [[1, 2, 3], 4, 5]
l_copy = l_original.copy()

# l_originalとl_copyは違うアドレスになっている
print(id(l_original), id(l_copy))

# l_original[0]とl_copy[0]は同じアドレスになっている
print(id(l_original[0]), id(l_copy[0]))
print("*****")

# l_originalとl_copyの両方が変わってしまう
l_original[0][1] = 100
print(l_original, l_copy) # [[1, 100, 3], 4, 5] [[1, 100, 3], 4, 5]
print("*****")


# copy
import copy

l_original = [[1, 2, 3], 4, 5]
l_copy = copy.deepcopy(l_original)

# l_originalとl_copyは違うアドレスになっている
print(id(l_original), id(l_copy))

# l_original[0]とl_copy[0]も違うアドレスになっている
print(id(l_original[0]), id(l_copy[0]))
print("*****")
