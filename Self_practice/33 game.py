import random



def add_number():
    number = random.randint(1,10)
    return number


def main():
    player_score = 0

    player_choice = input('Do you want to add number:Y/N').capitalize()

    while player_choice == "Y":
        player_score += add_number()
        player_choice = input('Do you want to add number:Y/N').capitalize()
    if player_choice == "N":
        if player_score < 24 or player_score > 33:
            print(f"You Failed the game, Your score is {player_score}")
        else:
            total_point = 10 * (player_score- 23)
            print(f"Your score is {total_point}")
    else:
        print('Incorrect input')
        player_choice = input('Do you want to add number:Y/N').capitalize()


main()






