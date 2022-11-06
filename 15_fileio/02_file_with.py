# withを使えばcloseしなくてもOK
with open("test.txt", encoding="utf-8", mode="a") as my_file:
    my_file.write("Hi there")

with open("test/test2.txt", encoding="utf-8", mode="a") as my_file:
    my_file.write("Hi there")
