my_file = open("myfile.txt", "w")

print("Type: ", type(my_file))
print("Name: ", my_file.name)
print("Is Closed: ", my_file.closed)
print("Opening Mode: ", my_file.mode)

my_file.write("I love python")
my_file.write(" And javascript.")
my_file.close()

# appendモード
my_file = open("myfile.txt", "a")
my_file.write(" I also like PHP.")
my_file.close()

# readモード
my_file = open("myfile.txt", "r+")
text = my_file.read(10)
print(text)