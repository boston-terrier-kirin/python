def get_total(**kwargs):
    # kwargsはdictになっている
    print(kwargs)

    sum = 0
    for value in kwargs.values():
        sum += value
    
    print(sum)

get_total(a=1, b=2, c=3)
