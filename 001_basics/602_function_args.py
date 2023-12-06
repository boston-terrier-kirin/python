def get_total(*args):
    # argsはtupleになっている
    print(args)
    print(sum(args))


get_total(1, 2, 3, 4, 5)
print("*******************")

# *でtupleの展開
param = (1, 2, 3, 4, 5)
get_total(*param)
print("*******************")

# *でlistの展開
param = [1, 2, 3, 4, 5]
get_total(*param)
print("*******************")


# *argsは省略できる 
def login(first, *args):
    print(first, args)


login("kirin")
login("kirin", "kuroro")
print("*******************")


# *argsの後ろにcを追加できる
def func(a, b, *args, c):
    print(a, b, args, c)


# これはできない
# TypeError: func() missing 1 required keyword-only argument: 'c'
# func(1, 2, 3, 4, 5, 6)

# *argsの後ろは、namedにする必要がある
# 1 2 (3, 4, 5) 6
func(1, 2, 3, 4, 5, c=6)
print("*******************")


# *以降は、namedを強制することになる
def func(a, b, *, c, d):
    print(a, b, c, d)


# TypeError: func() takes 2 positional arguments but 4 were given
# func(1, 2, 3, 4)

func(1, 2, c=3, d=4)
print("*******************")


# *以降は、namedを強制することになるので、これで全部がnamed
def func(*, a, b, c, d):
    print(a, b, c, d)


func(a=1, b=2, c=3, d=4)
print("*******************")


# defaultありの後ろにpositionalはおくと、defaultを省略できなくなって困るので、シンタックスエラーになる
# SyntaxError: non-default argument follows default argument
# def func(a, b=1, c):
#     print(a, b, c)
