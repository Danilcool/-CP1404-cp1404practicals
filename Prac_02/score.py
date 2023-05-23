import random

def main():
    score = float(input("Enter score: "))
    get_result(score)

    get_result(random.randint(1,100))

def get_result(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")

main()