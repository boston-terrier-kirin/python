animal = "dog"


def outer():
    # これはOK
    animal = "cat"
    print("outer: ", animal)

    def inner():
        # これでglobalを書き換えられる
        global animal
        animal = "bird"
        print("inner: ", animal)

    inner()


outer()
print(animal)
