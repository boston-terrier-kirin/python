users = [
    {"username": "kirin", "tweets": ["I hate dogs"]},
    {"username": "kuroro", "tweets": ["I love dogs", "I love human"]},
    {"username": "stephen", "tweets": []},
    {"username": "draymond", "tweets": ["punch"]},
    {"username": "klay", "tweets": []},
]

max_tweeted_user = max(users, key=lambda u: len(u["tweets"]))
print(max_tweeted_user)