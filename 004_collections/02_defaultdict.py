# 同じ文字が何回登場するかをカウントする
words = "aabbaca"

# not inでキーがなければ初期値をセット
words_dict = {}
for word in words:
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1

print(words_dict)
print("***************")

# setdefaultで初期値をセット
words_dict = {}
for word in words:
    words_dict.setdefault(word, 0)
    words_dict[word] += 1

print(words_dict)
print("***************")

# defaultdict *keyがない場合の初期値を指定できる
from collections import defaultdict
words_dict = defaultdict(int)
for word in words:
    words_dict[word] += 1

print(words_dict)