my_file = open("test/test.txt", encoding="utf-8")

print(my_file)

print(my_file.read())
print("---------------------------")

# seek(0)で先頭に戻ってくれる
my_file.seek(0)

# 1行だけ
print(my_file.readline())
my_file.seek(0)

# 配列
print(my_file.readlines())

my_file.close()
