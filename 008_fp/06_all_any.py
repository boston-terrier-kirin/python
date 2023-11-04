people = ["Step", "Klay", "Kuroro", "Kirin"]

# false, true, true, true
print([name[0] == "K" for name in people])

# all
result = all([name[0] == "K" for name in people])
print(result)

# any
result = any([name[0] == "K" for name in people])
print(result)
