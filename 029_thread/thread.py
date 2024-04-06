import time
from threading import Thread


def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user: {time.time() - start}")


def complex_calc():
    start = time.time()
    print("Start calc...")
    [x**2 for x in range(20000000)]
    print(f"complex_calc: {time.time() - start}")


start = time.time()
t1 = Thread(target=complex_calc)
t2 = Thread(target=ask_user)

t1.start()
t2.start()

t1.join()
t2.join()
print(f"Total: {time.time() - start}")


