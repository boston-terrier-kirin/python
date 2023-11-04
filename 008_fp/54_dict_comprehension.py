players = {}
players["stephen"] = 30
players["clay"] = 11
players["draymond"] = 23

my_dict = {k.upper(): v * 2 for k, v in players.items()}

print(my_dict)
