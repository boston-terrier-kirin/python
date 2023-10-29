# https://docs.python.org/3/library/exceptions.html

try:
    age = int(input("what is your age? :"))
    10 / age

except ValueError as err:
    print("please enter a number", err)
except ZeroDivisionError as err:
    print("please enter a number except 0", err)

# ここもブロックスコープではない
print(f"your age is ", age)
