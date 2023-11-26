def zoo():
    animal = "Harle"
    print("INSIDE zoo FUNC", animal)

    def inner():
        print("INSIDE inner FUNC", animal)

    inner()


zoo()

# これはもちろんエラー
# print("OUTSIDE zoo FUNC", animal)

# これはできる
if True:
    animal = "Osprey"

print("AFTER IF", animal)
