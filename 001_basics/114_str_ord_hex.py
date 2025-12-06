# [A] https://www.compart.com/en/unicode/U+0041
# [α] https://www.compart.com/en/unicode/U+03B1
# [🐍] https://www.compart.com/en/unicode/U+1F40D

# 10進数で表示
print(ord("A"))
print(ord("α"))
print(ord("🐍"))
print("*" * 10)

# 16進数で表示
print(hex(ord("A")))
print(hex(ord("α")))
print(hex(ord("🐍")))
print("*" * 10)

# 16進数を10進数に戻す
print(int("3b1", 16))
print("*" * 10)

# 名前で指定する
by_name = "\N{Snake} scares me!"
print(by_name)

# コードで指定する *\uの場合は、0埋めして4桁にする
by_code = "\u0041"
print(by_code)

# コードで指定する *\Uの場合は、0埋めして8桁にする
by_code = "\U00000041"
print(by_code)

by_code = "\U0001F40D scares me!"
print(by_code)
