def my_func():
    # これでmoduleレベルの変数になってしまう
    global x
    x = 10


my_func()

print(x)
