def counter():
    num = 0

    def countup():
        nonlocal num
        num += 1
        print(num)

    return countup


my_counter = counter()

my_counter()
my_counter()
my_counter()
my_counter()
my_counter()
