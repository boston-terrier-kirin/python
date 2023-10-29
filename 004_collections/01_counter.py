from collections import Counter

my_list = [1, 1, 1, 2, 2, 3, 3, 3, 3]
c = Counter(my_list)

print(c)
print("***************")

print(c[3])
print("***************")

for item in c:
    print(item, c[item])
print("***************")

# 頻度の高い順
print(c.most_common())
print("***************")

# 一番頻度の高いやつ
print(c.most_common(1))
