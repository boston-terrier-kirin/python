ranks = {
    "John": 95,
    "Jane": 67,
    "Tim": 92,
    "Steph": 98
}

print(sorted(ranks, reverse=True, key=ranks.get))
print("*************************************")

ranks = [
    {"name": "John", "point": 95},
    {"name": "Jane", "point": 67},
    {"name": "Tim", "point": 92},
    {"name": "Steph", "point": 98},
]

print(sorted(ranks, reverse=True, key=lambda d: d["point"]))
print("*************************************")
