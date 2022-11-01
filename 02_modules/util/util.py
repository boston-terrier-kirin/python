def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# util.py を直接実行すると、__main__ になる。
print(__name__)

# main として直接実行された場合のみ処理を走らせたい時に使うらしい。
if (__name__ == "__main__"):
    print("===== test =====")
    result = multiply(10, 5)
    print("should be 50: ", result)
    
    result = divide(10, 5)
    print("should be 2.0: ", result)