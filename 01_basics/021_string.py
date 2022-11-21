first_name = "Kuroro"
last_name = "Matsumoto"
age = 2

# これはできない
# print(first_name + " " + last_name + ", Age:" + age )

print(first_name + " " + last_name + ", Age:" + str(age))
print("*************************************")

# これで文字列の繰り返しができる
print(first_name * 10)
print("*************************************")

print(first_name[0])
print("*************************************")

length = len(last_name)
print(last_name[length-1])
# これでもOK
print(last_name[-1])
print("*************************************")

# None
user = None
print(user)
print(type(user))
print("*************************************")

# slice
# 012345678
# Matsumoto
print(last_name[0:2])
print(last_name[2:5])
print(last_name[2:])
print(last_name[0:5])
print(last_name[:5])
print("*************************************")

woid = "KSB123456789"
print(woid[3:])
print("*************************************")

# escape
print("Hello\nWorld")
print("Hello\tWorld")
print('O\'NEILL')
print("*************************************")

# """
lorem = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book."""
print("->",lorem)
print("*************************************")

# """ + \
lorem = """\
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.\
"""
print("->",lorem)
print("*************************************")

# \ だけだと改行はされない
lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry." \
        "Lorem Ipsum has been the industry's"
print("->",lorem)
print("*************************************")

# () でもOK
lorem = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry."
        "Lorem Ipsum has been the industry's")
print("->",lorem)
print("*************************************")

# escapeしなくても良い
print("""O'NEILL""")