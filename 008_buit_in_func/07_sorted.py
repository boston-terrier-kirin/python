# sortの場合
nums = [4, 1, 3, 6, 5, 2]
nums.sort()
print("mutable", nums)

# sortedの場合
nums = [4, 1, 3, 6, 5, 2]
sorted_nums = sorted(nums)
print("immutable", nums, sorted_nums)

# reverse
nums = [4, 1, 3, 6, 5, 2]
reversed_nums = sorted(nums, reverse=True)
print("reverse", nums, reversed_nums)

# reversed はiteratorを返す
nums = [4, 1, 3, 6, 5, 2]
reversed_nums = reversed(nums)
print("reversed", nums, reversed_nums)

word = "abcde"
print("reversed", "".join(reversed(word)))

# tuple1のソート
ts = (4, 1, 3, 6, 5, 2)
print("listになる", sorted(ts))

# objectのソート
users = [
    {"username": "kirin", "tweets": ["I hate dogs"]},
    {"username": "kuroro", "tweets": ["I love dogs", "I love human"]},
    {"username": "stephen", "tweets": []},
    {"username": "draymond", "tweets": ["punch"]},
    {"username": "klay", "tweets": []},
]

# usernameでsort
sorted_users = sorted(users, key=lambda user: user["username"])
print(sorted_users)

# tweet数でsort
sorted_users = [u["username"] for u in sorted(users, key=lambda user: len(user["tweets"]), reverse=True)]
print(sorted_users)
