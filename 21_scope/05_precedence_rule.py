animal = "dog"


def outer():
    # これはOK
    animal = "cat"
    print("outer: ", animal)

    def inner():
        # ここで宣言すると、innerの中の変数になる
        animal = "bird"
        print("inner: ", animal)

    def inner2():
        # ここはouterのanimalを見に行くので、car
        print("inner2: ", animal)

    inner()
    inner2()


def outer2():
    print(animal)
    # これはNG。UnboundLocalError: local variable 'animal' referenced before assignment
    # animal = "dog"


outer()
outer2()
