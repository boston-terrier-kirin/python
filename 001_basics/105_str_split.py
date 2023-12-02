name = "kohei    matsumoto"

# jsのsplitとはちょっと違う
# ['kohei', '', '', '', 'matsumoto']
print("name.split(' ')", name.split(" "))
print("*************************************")

# これはできない
# ValueError: empty separator
# print(name.split(""))

# name.split("")がやりたい場合は、list(name)で配列になる
# ['k', 'o', 'h', 'e', 'i', ' ', ' ', ' ', ' ', 'm', 'a', 't', 's', 'u', 'm', 'o', 't', 'o']
print("list(name)", list(name))
print("*************************************")

# list comprehensionで空白をのぞく
print("list comprehension", [char for char in list(name) if char != ' '])
print("*************************************")

# 間にあるスペースを無視する場合、name.split()
# ['kohei', 'matsumoto']
print("name.split()", name.split())
print("*************************************")

# str自体が最初からiterableなので、1文字づつ処理したい場合はforを使う
for letter in name:
    print(letter)
