a = "Hello"

def test():
    print(a)

test()
print("***************")

count = 0

def counter():
    # 意外にもこれはできない
    # UnboundLocalError: local variable 'count' referenced before assignment
    # count += 1
    pass

counter()
print("***************")

def counter2():
   global count
   count += 1
   return count

print(counter2())
print(counter2())