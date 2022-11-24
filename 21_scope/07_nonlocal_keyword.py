animal = "dog"


def outer():
    # これはOK
    animal = "cat"

    def inner():
        # これでouterのanimalを書き換えられる
        nonlocal animal
        animal = "bird"
        print("inner: ", animal)

    inner()
    print("outer: ", animal)


outer()
print(animal)
