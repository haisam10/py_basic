# Sequence Types  :	list, tuple, range
print("\n")
# list type data ==========
print("============ ist type data ============")
li = ['admin_1', 'admin_2', 'admin_3']
print(li)
print(type(li))

li[1] = 'admin_5' # value change ==========
print(li)
print("\n")

# tuple type data ==========
print("============ tuple type data ============")
tple = (1, 2, 3, 4, 5)
print(tple)
print(type(tple))
print("\n")

# range type data ==========
print("============ range type data ============")
rmg = range(10)
print(rmg)

for i in rmg:
    print(i)
