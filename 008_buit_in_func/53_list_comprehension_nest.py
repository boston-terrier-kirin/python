dogs = [
    ["Kirin", "16"],
    ["Kuroro", "3"]
]

converted = [[item.upper() for item in dog] for dog in dogs]
print(converted)

converted = [dog[0].upper() for dog in dogs]
print(converted)

converted = map(lambda dog: dog[0].upper(), dogs)
print(list(converted))
