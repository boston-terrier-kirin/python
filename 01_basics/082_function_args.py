def get_total(*args):
    # argsはtupleになっている
    print(args)

    print(sum(args))

get_total(1, 2, 3, 4, 5)
