duos = [
    ["Steph", "Clay"],
    ["AD", "Lebron"]
]
duos2 = duos[:]

# : はshallow copyなので、ネストした配列は同じポインタになっている。
print("id", id(duos), id(duos2))
print("id", id(duos[0]), id(duos2[0]))

# これはduosのみ変わる
duos.append(["Tatum", "Brown"])
print(duos, "---", duos2)

# [0]に追加すれば、duos2に追加されてしまう。
duos[0].append("Draymond")
print(duos, "---", duos2)
print("***************")

# cppy
import copy
duos = [
    ["Steph", "Clay"],
    ["AD", "Lebron"]
]
duos2 = copy.deepcopy(duos)

print("id", id(duos), id(duos2))
print("id", id(duos[0]), id(duos2[0]))

duos.append(["Tatum", "Brown"])
print(duos, "---", duos2)

duos[0].append("Draymond")
print(duos, "---", duos2)