# 03_custom_iterator.pyではclassを使って状態をkeepしていたが、generatorを使えば勝手に状態保持してくれる
# generatorはiteratorのサブセット
def count_up_to(max_value):
    # このcounterを状態保持してくれる
    count = 1

    while count <= max_value:
        yield count
        count += 1


counter = count_up_to(5)

# <generator object count_up_to at 0x000001B365FC4E40>
print(counter)

for num in count_up_to(5):
    print(num)

print("*****")

# listに変換することも可能
print(list(count_up_to(5)))
