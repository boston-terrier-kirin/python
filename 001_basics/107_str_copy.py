text_a = "aaaaa"

text_c = text_a
text_c = "ccccc"

# aaaaa ccccc
print(text_a, text_c)

# [:]でコピーできる
text_b = text_a[:]
print(text_a, text_b)
