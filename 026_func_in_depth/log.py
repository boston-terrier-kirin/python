import time
from datetime import datetime


# デフォルト値はモジュールが呼ばれ時に評価されるので、何回呼び出してもdtの値は同じになってしまう。
def log1(msg, *, dt=datetime.utcnow()):
    print(f"{msg}: {dt}")


log1("Hello")
time.sleep(1)
log1("Hello")
time.sleep(1)
log1("Hello")
time.sleep(1)
print("*****")


# デフォルト値を固定したくない場合は、Noneにしておく。
def log2(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f"{msg}: {dt}")


log2("Hello")
time.sleep(1)
log2("Hello")
time.sleep(1)
log2("Hello")
time.sleep(1)
