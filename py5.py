# Binary Types    :	bytes, bytearray, memoryview
print("\n")
''' Binary Types data range '0' to '255' it's limit  '''
print('===== byte =====')
x = [1, 2, 3, 4, 5, 6, 7, 50, 56, 80, 112, 200, 244]
print(x)
y = bytes(x)
print(type(y))
print("\n")

print('===== byte array ===== ')
x = [1, 2, 3, 4, 5, 6, 7, 50, 56, 80, 112, 200, 244]
x = bytearray(x)
print(type(x))
print("\n")

print('===== change array ===== ')
x[2] = 100
x[4] = 230
print(x[2])
print(x[4])

'''======================================='''