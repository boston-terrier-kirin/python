def zoo():
    animal = "Harle"
    print("INSIDE zoo FUNC", animal)

    def inner():
        # localスコープ的に考えると若干不思議な気がするが、これはできる。
        print("INSIDE inner FUNC", animal)

    inner()


zoo()
