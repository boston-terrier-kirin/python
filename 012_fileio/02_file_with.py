# withを使えばcloseしなくてもOK
with open("test.txt", encoding="utf-8", mode="a") as my_file:
    my_file.write("Hi there")

# 上書き
with open("test/test2.txt", encoding="utf-8", mode="w") as my_file:
    my_file.write("Hi Kuroro")
    my_file.write("\n")

# append
with open("test/test2.txt", encoding="utf-8", mode="a") as my_file:
    my_file.write("Hi Kirin")
