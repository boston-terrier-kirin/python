def outer():
    x = "outer"

    def inner():
        x = "inner"
        print("inner", x)
    
    inner()
    print("outer", x)

outer()
print("***************")

def outer2():
    x = "outer"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)
    
    inner()
    print("outer", x)

outer2()