s = {1, 2, 3}

# removeは存在しないキーを指定するとエラーになる。
try:
    s.remove(99)
except KeyError:
    print("Error")

# discardはエラーにならない。
s.discard(99)
