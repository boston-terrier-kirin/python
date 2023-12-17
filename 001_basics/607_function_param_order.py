# 1. parameters
# 2. *args
# 3. default parameters
# 4. **args

def display_info(a, b, *args, instructor="Colt", **kwargs):
    print(f"a={a}, b={b}, args={args}, instructor={instructor}, kwargs={kwargs}")


display_info(1, 2, 3, last_name="Steele", job="instructor")
