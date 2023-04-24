def get_ranges():
    global i
    for i in range(1, 21, 2):
        print(i, end=' ')
    print("\n")
    for i in range(0, 110, 10):
        print(i, end=" ")
    print("\n")
    for i in range(20, 0, -1):
        print(i, end=" ")


get_ranges()

print("\n")


def get_star_number():
    global stars, i
    stars = int(input("Number of stars:"))
    for i in range(stars):
        print("*", end="")


get_star_number()




def get_star_rows():
    global stars, i
    stars = int(input("Number of star rows:"))
    star = '*'
    for i in range(stars):
        print(star)
        star += "*"


get_star_rows()
