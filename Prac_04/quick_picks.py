import random

LOW_NUMBER = 1
HIGH_NUMBER = 45
RANDOM_NUMBER = 6

user_quick_picks = int(input("How many quick picks? "))
for number in range(user_quick_picks):
    number_list = []
    while len(number_list) != 6:
        random_number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        if random_number not in number_list:
            number_list.append(random_number)

    number_list.sort()
    print(" ".join("{:2d}".format(number) for number in number_list))