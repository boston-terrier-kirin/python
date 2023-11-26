for char in "OCTOPUS":
    pass

# forの外でもcharが見えるので、S になる
print("AFTER for", char)


for num in range(10):
    x = num

# forの外でもxが見えるので、9 になる
print("AFTER for", x)