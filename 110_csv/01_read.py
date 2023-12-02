from csv import reader

with open("fighters.csv") as file:
    csv_reader = reader(file, delimiter=",")

    # generatorになっている
    for row in csv_reader:
        print(row)

print("*****")

with open("fighters.csv") as file:
    csv_reader = reader(file, delimiter=",")

    # generatorになっているので、listに変換できる
    fighters = list(csv_reader)
    print(fighters)
