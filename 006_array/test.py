# https://docs.python.org/3.11/library/array.html
from array import array

# listより性能が良いらしい
arr = array("i", [1, 2, 3])

print(arr)
print(arr[0])
