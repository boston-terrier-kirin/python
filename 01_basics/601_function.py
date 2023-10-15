def get_total(price, qty=1, tax=0.1, discount=0):
    subtotal = price * qty * (1 - discount)
    print(subtotal * (1 + tax))


get_total(100)

# named parameter
# pythonでは何もしなくてもnamedになる。
get_total(100, qty=2)
get_total(price=100, qty=2)
get_total(tax=0.2, price=100, qty=2)
