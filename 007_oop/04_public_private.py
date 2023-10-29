class PlayerCharactor:
    def __init__(self, name, age):
        # pythonではprivateがないので、_ をつける
        self._name = name
        self._age = age

    def run(self):
        print(f"My name is {self._name}, {self._age} years old.")


player_1 = PlayerCharactor("Tim", 27)
player_1.run()
