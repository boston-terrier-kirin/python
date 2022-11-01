# str.strip([chars])
# [chars] はoptional

print('www.example.com'.strip('www.'))

print('www.example.com'.strip('www.com'))

# 先頭・最終の、なので、これではうまくいかない
print('   www.example.com   '.strip('.wcom'))

print('   www.example.com   '.strip(' .wcom'))