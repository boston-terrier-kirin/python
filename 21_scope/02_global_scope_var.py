# 数字で始まる場合は、__import__ を使う
global_scope =  __import__("01_global_scope")

# globalスコープの変数は呼び出せる
print(global_scope.animal)
