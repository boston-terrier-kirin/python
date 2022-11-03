# https://docs.python.org/3.11/library/datetime.html
from time import time
import datetime
from datetime import date

st = time()

print(datetime.time(7, 54, 30))
print(datetime.date.today())

print(date.today())

en = time()
print(en - st)
