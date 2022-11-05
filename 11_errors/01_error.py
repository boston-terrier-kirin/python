# https://docs.python.org/3/library/exceptions.html

try:
    age = int(input("what is your age? :"))

# Exceptionを指定しないのもあり
except:
    print("please enter a number")
