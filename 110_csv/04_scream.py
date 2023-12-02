from csv import reader, writer

# 方法その1
with open("fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[col.upper() for col in row] for row in csv_reader]

with open("new_fighters.csv", "w", newline="") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

# 方法その2
with open("fighters.csv") as file:
    csv_reader = reader(file)

    with open("new_fighters_2.csv", "w", newline="") as w_file:
        csv_writer = writer(w_file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
