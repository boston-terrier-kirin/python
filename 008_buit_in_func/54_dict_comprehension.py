players = {}
players["stephen"] = 30
players["clay"] = 11
players["draymond"] = 23

print("***** dict items")
for k, v in players.items():
    print(k, v)

print("***** dict comprehension")
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
my_dict = {k.upper(): v * 2 for k, v in players.items()}

print(my_dict)
