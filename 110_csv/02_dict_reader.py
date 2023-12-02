from csv import DictReader

with open("fighters.csv") as file:
    csv_reader = DictReader(file, delimiter=",")

    for row in csv_reader:
        print(row)

