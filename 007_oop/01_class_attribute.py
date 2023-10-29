class PlayerCharactor:
    # Class Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        # membershipはClass自体の属性になっているが、selfで参照してしまえるのが、ややこしい。
        print(f"Run {self.name}, {PlayerCharactor.membership} {self.membership}")


player_1 = PlayerCharactor("Cindy", 24)
# membershipはClass自体の属性になっているが、インスタンスごとに変えることもできるらしい。
player_1.membership = False
player_1.run()
print("*************************************")

player_2 = PlayerCharactor("Tim", 24)
player_2.run()
print("*************************************")

# とちらかと言えば、static変数のような使い方をする
print(PlayerCharactor.membership)
# PlayerCharactorを変えれば、各インスタンスの値も変わる
PlayerCharactor.membership = False

player_1.run()
player_2.run()