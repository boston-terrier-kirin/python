# sequence types
l = [1, 2, 3]
s = "python"
t = (1, 2, 3)

print(l[0], s[2], t[2])
print("*****")


# setはiterableだけど、sequence typeではない。
s = {"x", 10, "a", "A"}

# ループはできるが、インデックス指定ではアクセスできない。
for e in s:
    print(e)
