class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass

# 1になる
print(D.num)

# D -> B-> C-> A
# <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>
print(D.mro())
