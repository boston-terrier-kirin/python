users = [
    {"username": "kirin", "tweets": ["I hate dogs"]},
    {"username": "kuroro", "tweets": ["I love dogs", "I love human"]},
    {"username": "stephen", "tweets": []},
    {"username": "draymond", "tweets": ["punch"]},
    {"username": "klay", "tweets": []},
]

# filter -> map バージョン
inactive_users_1 = list(map(lambda u: u["username"],
                          filter(lambda u: not u["tweets"], users)))
print(inactive_users_1)

# list comprehension バージョン
inactive_users_2 = [user["username"] for user in users if not user["tweets"]]
print(inactive_users_2)
