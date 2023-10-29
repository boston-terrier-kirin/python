class PlayerCharactor:
    # Class Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"Run {self.name}")

    @staticmethod
    def add(num1, num2):
        # clsがないバージョン
        return num1 + num2


player_1 = PlayerCharactor("Tim", 27)
player_1.run()

print(player_1.add(3, 7))
