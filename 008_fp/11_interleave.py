def interleave(s1, s2):
    return "".join([char[0] + char[1] for char in zip(s1, s2)])


print(interleave("hi", "ha"))
print(interleave('aaa', 'zzz'))
print(interleave('lzr','iad'))
