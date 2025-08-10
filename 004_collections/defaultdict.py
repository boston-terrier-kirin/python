from collections import defaultdict


cowokers = [("Rolf", "MIT"), ("Jen", "Oxford"), ("Rolf", "UCLA")]

# dictのデフォルト値がlistになる
merged = defaultdict(list)

for cowoker, place in cowokers:
    merged[cowoker].append(place)

print(merged)
print("-----")

# これと同じこと
merged = {}
for cowoker, place in cowokers:
    places = merged.get(cowoker, [])
    places.append(place)
    merged[cowoker] = places

print(merged)