points = [1140, -1140, 0]

mail_body = """決済総額: {0}
ポイント/キャッシュ利用: {1}
お支払金額: {2}
""".format(*points)

# * は、list unpacking。こういう時にも使える
print(mail_body)
print("*************************************")

print(points)
print("*************************************")

print(*points)
print("*************************************")

# 順番だけではなく、キーワードでも使える
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
print("*************************************")

# float
result = 100 / 777
print(result)

# {value:width.precision f}
print("The result was {r:1.3f}".format(r=result))
