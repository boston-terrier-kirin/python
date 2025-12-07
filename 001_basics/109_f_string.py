# f-stringはpython3.6からできた新しい機能。もとは、formatを使っていた。
first_name = "Kuroro"
last_name = "Matsumoto"
age = 2

print(f"Hi, {first_name} {last_name} Age: {age}")
print("*" * 10)

bid = 1.5760
ask = 1.5763
print(f"bid: {bid:.4f}, ask: {ask:.4f}, spread: {(ask - bid):.4f}")
