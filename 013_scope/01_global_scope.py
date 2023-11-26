animal = "Lemur"

print("OUTSIDE OF FUNCTION", animal)


def func():
    print("INSIDE OF FUNCTION", animal)

    def inner():
        print("INSIDE OF INNER FUNCTION", animal)

    inner()


if __name__ == "__main__":
    func()
