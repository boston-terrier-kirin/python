class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Login")


class Wizard(User):
    def __init__(self, name, email, power):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} {self.email} : Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, email, num_arrows):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(
            f"{self.name} {self.email} : Attacking with arrows: arrows left - of {self.num_arrows}")


player_1 = Wizard("Tim", "tim@test.com", 300)
player_1.sign_in()
player_1.attack()

player_2 = Archer("Robin", "tim@test.com", 30)
player_2.sign_in()
player_2.attack()
print("*************************************")

# pythonでもこれができる
users = [player_1, player_2]
for user in users:
    user.attack()
print("*************************************")

print(isinstance(player_1, object))
print(isinstance(player_1, User))
print(isinstance(player_1, Wizard))
print(isinstance(player_1, Archer))
print("*************************************")

print(dir(player_1))
