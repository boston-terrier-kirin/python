d = {
    "kirin": {"age": 15},
    "kuroro": {"age": 3}
}

# jsの||と同じことができる
kohei = d.get("kohei") or {}

d["kohei"] = {
    "age": 47
}

print(d)


# DBから取得したnameがNoneの場合にエラーになるのを防ぐ
import string
name = None

if name and name[0] in string.digits:
    print("Name cannot start with a digit.")

# len(name)だとNoneに対応できない
# TypeError: object of type 'NoneType' has no len()
# if len(name) > 0 and name[0] in string.digits:
#     print("Name cannot start with a digit.")
