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