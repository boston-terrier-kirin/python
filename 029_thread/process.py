import time
from multiprocessing import Process


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


process = Process(target=complex_calc)
process.start()

start = time.time()
ask_user()
process.join()

print(f"Total time: {time.time() - start}")
