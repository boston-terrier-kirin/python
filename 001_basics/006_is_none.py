value_1 = None

if not value_1:
    print("None-1")

if value_1 is None:
    print("None-2")

# これはうまくいかない。is はNoneを判定するのに有効。
value_2 = []
if value_2 is "":
    print("Empty")
