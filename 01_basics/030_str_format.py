points = [1140, -1140, 0]

mail_body = """決済総額: {0}
ポイント/キャッシュ利用: {1}
お支払金額: {2}
""".format(*points)

# * は、list unpacking。こういう時にも使える
print(mail_body)

print(points)
print(*points)
