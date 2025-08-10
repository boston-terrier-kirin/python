from collections import deque

friends = deque(("Steph", "Klay", "Tim"))
friends.append("Jose")
friends.appendleft("Anthony")

print(friends)
print("-----")

# 右から削除
friends.pop()
print(friends)
print("-----")

# 左から削除
friends.popleft()
print(friends)
print("-----")
