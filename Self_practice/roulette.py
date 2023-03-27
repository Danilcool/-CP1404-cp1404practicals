import random

def roll_roulette():
    return random.randint(0,10)

def main():
    player_chips = 10
    options = {'G': 'Green', 'B': 'Black', 'R': 'Red'}

    while player_chips > 0:
        print(f'Your chips: {player_chips}')
        user_input = input(f"Select a color ({', '.join([f'({k}){v}' for k,v in options.items()])}): ")
        while user_input not in options:
            print("Invalid input, try again.")
            user_input = input(f"Select a color ({', '.join([f'({k}){v}' for k,v in options.items()])}): ")
        user_bet = int(input("What is your bet? "))

        if user_bet > player_chips:
            print("Sorry, you don't have enough chips.")
            continue

        roll = roll_roulette()
        print(f"The roulette rolled: {roll}")

        if roll == 0 and user_input == "G":
            print(f"Congratulations! You won {user_bet*7} chips!")
            player_chips += user_bet * 7
        elif roll % 2 == 0 and user_input == "B":
            print(f"Congratulations! You won {user_bet*2} chips!")
            player_chips += user_bet * 2
        elif roll % 2 == 1 and user_input == "R":
            print(f"Congratulations! You won {user_bet*2} chips!")
            player_chips += user_bet * 2
        else:
            print("Sorry, you lost.")
            player_chips -= user_bet

    print("Game over.")

if __name__ == '__main__':
    main()