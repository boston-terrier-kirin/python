# https://docs.python.org/3.11/library/datetime.html
import datetime
from datetime import date
from time import time

st = time()

print(datetime.time(7, 54, 30))
print(datetime.date.today())
print("*****")

today = date.today()
print(type(today))
print(today)
print(today.year)
print(today.month)
print(today.day)
print("*****")

en = time()
print(en - st)
