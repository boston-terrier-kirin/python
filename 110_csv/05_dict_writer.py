from csv import DictWriter

with open("dogs.csv", "w", newline="") as file:
    headers = ["Name", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Kirin",
        "Age": 16
    })
    csv_writer.writerow({
        "Name": "Kuroro",
        "Age": 3
    })
