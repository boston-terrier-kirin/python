val_1 = [1, 2, 3, 4]
val_2 = [3, 4, 5, 6]

answer = [value for value in val_1 if value in val_2]
print(answer)

# loopで書くとこうなる
answer = []
for value in val_1:
    if value in val_2:
        answer.append(value)

print(answer)
