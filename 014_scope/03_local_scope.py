def zoo():
    animal = "Harle"
    print("INSIDE zoo FUC", animal)

    def inner():
        print("INSIDE inner FUC", animal)

    inner()


zoo()

# これはもちろんエラー
# print("OUTSIDE zoo FUC", animal)

# これはできる
if True:
    animal = "Osprey"

print("AFTER IF", animal)

for char in "OCTOPUS":
    pass

print("AFTER for", char)
