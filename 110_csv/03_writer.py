from csv import writer, reader

with open("dogs.csv", "w", newline="") as file:
    csv_writer = writer(file)

    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Kirin", 16])
    csv_writer.writerow(["Kuroro", 3])

print("*****")

with open("dogs.csv") as file:
    csv_reader = reader(file, delimiter=",")

    # generatorになっているので、listに変換できる
    fighters = list(csv_reader)
    print(fighters)