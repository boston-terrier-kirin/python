def hello(name="Kirin"):
    print(f"Hello {name}")

    def greet():
        print(f"This is the greet {name}")

    return greet


func = hello()
func()
