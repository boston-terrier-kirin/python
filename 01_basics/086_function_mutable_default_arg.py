def func(num, lst=[]):
    lst.append(num)
    lst.append(num)
    print(lst)

def func2(num, lst=None):
    if lst is None:
        lst = []

    lst.append(num)
    lst.append(num)
    print(lst)

# [10, 10]
func(10)

# lstがシェアされてしまうので、こうなってしまう。
# [10, 10, 20, 20]
func(20)

# listをデフォルト値にするのであれば、func2みたいにする。
func2(10)
func2(20)