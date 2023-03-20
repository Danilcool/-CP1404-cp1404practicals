


def get_result(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")

def get_valid_score(score):
    if score > 0 and score < 101:
        print("Valid")
    else:
        print("Invalid")

def main():
    print("(G)et a valid score, (P)rint result, (S)how stars, (Q)uit")
    user_choice = input("Choice:").upper()

    while user_choice != "Q":
        score = int(input("Whats is your score:"))
        if user_choice == "G":
            get_valid_score(score)
            print("(G)et a valid score, (P)rint result, (S)how stars, (Q)uit")
            user_choice = input("Choice:").upper()
        elif user_choice == "P":
            get_result(score)
            print("(G)et a valid score, (P)rint result, (S)how stars, (Q)uit")
            user_choice = input("Choice:").upper()
        elif user_choice == "S":
            for i in range(score):
                print("*",end="")
            print("(G)et a valid score, (P)rint result, (S)how stars, (Q)uit")
            user_choice = input("Choice:").upper()
        else:
            print("Invalid Score")
            score = int(input("Whats is your score:"))

    print("Farewell")
main()