my_file = open("test/test.txt", encoding="utf-8")

print(my_file)

print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)

print(my_file.readline())
my_file.seek(0)

print(my_file.readlines())
my_file.seek(0)

my_file.close()
