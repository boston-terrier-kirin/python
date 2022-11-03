class PlayerCharactor:
    # Class Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"Run {self.name}")

    @classmethod
    def register(cls):
        # これでClass Attributeを参照可能
        print(f"Yo! Membership: {cls.membership}")

        # これはできない
        # cls.run()
        # run()

        # clsはclass自体なので、これで新しいインスタンスが作れる
        return cls("John", 25)
    
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2


player_1 = PlayerCharactor("Tim", 27)
player_1.run()

print(player_1.add(1, 2))

player_2 = PlayerCharactor.register()
player_2.run()
