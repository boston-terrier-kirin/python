import os
import shutil

print(os.getcwd())
print("*****")

print(os.listdir())
print("*****")

print(os.listdir("C:\\Users"))
print("*****")

# 既にファイルがあれば削除して、テスト用のファイルを作成
if os.path.isfile("move_to\\test.txt"):
    print("***** 既にファイルがあれば削除")
    os.unlink("move_to\\test.txt")

    print("***** テスト用のファイルを作成")
    f = open("test.txt", "w+")
    f.write("This is a test")
    f.close()

# 移動する
shutil.move("test.txt", "move_to")
