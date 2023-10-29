last_name = "Matsumoto"

# slice
# 012345678
# Matsumoto
print("[0:2]", last_name[0:2])
print("[2:5]", last_name[2:5])
print("[2: ]", last_name[2:])
print("[0:5]", last_name[0:5])
print("[ :5]", last_name[:5])
print("*************************************")

# last_name[start:end:step_size]
# 012345678
# M t u o o
print(last_name[0::2])
print("*************************************")

# step_sizeに-1を指定すれば、リバースできる
print(last_name[::-1])
print("*************************************")

woid = "KSB123456789"
print(woid[3:])
print("*************************************")
