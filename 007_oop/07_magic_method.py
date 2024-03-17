class Garage:
    def __init__(self):
        self.cars = []

    # toString相当
    def __repr__(self):
        return f"Garage: {self.cars}"

    # toString相当
    def __str__(self):
        return f"Garage with {self.cars}"

    # lenが使える
    def __len__(self):
        return len(self.cars)

    # [index]が使える
    def __getitem__(self, index):
        return self.cars[index]


my_garage = Garage()
my_garage.cars.append("Forester")
my_garage.cars.append("Levorg")

print(my_garage)

print(len(my_garage))
print(my_garage[0])
print("-----")

for car in my_garage:
    print(car)