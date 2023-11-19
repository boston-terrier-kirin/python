def get_total(**kwargs):
    # kwargsはdictになっている
    print(kwargs)

    sum = 0
    for value in kwargs.values():
        sum += value
    
    print(sum)


get_total(a=1, b=2, c=3)

# これはエラー
# get_total(1, 2, 3)

# **でdictの展開ができる
params = {
    "rakuten": 1250,
    "amazon": 500,
    "paypay": 5000
}

get_total(**params)