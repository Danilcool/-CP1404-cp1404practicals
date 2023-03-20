for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

for i in range(0, 110, 10):
    print(i, end=" ")
print("\n")

for i in range(20, 0, -1):
    print(i, end=" ")

print("\n")

stars = int(input("Number of stars:"))
for i in range(stars):
    print("*", end="")

print("\n")

stars = int(input("Number of star rows:"))
star = '*'
for i in range(stars):
    print(star)
    star += "*"
