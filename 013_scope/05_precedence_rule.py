animal = "dog"


def outer():
    # これはOK
    animal = "cat"
    print("outer: ", animal)

    def inner():
        # ここで宣言すると、innerの中の変数になる
        # outerを書き換えたい場合に使うのが、nonlocal
        animal = "bird"
        print("inner: ", animal)

    def inner2():
        # ここはouterのanimalを見に行くので、cat
        print("inner2: ", animal)

    inner()
    inner2()


def outer2():
    print(animal)

    # これはNG。UnboundLocalError: local variable 'animal' referenced before assignment
    # ここでanimalを定義すると、print(animal)もローカル変数扱いになってしまう
    # animal = "dog"


outer()
outer2()
