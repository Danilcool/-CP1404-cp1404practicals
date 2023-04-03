list_1 = []
list_2 = []
list_3 = []
list_4 = []
# [0, 1, 2, 3, 4, 5]
for i in range(6):
    list_1.append(i)

# [1, 5, 9, 13]
for i in range(1,14,4):
    list_2.append(i)

# [3, 2, 1]
for i in range(3,0,-1):
    list_3.append(i)

# [7, 4, 1, -2, -5]
for i in range(7,-6,-3):
    list_4.append(i)


print(list_1)
print(list_2)
print(list_3)
print(list_4)

