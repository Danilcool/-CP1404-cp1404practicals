import random

largestCountries = ["Russia","Canada","USA","China","Brazil","Australia","India","Argentina","Kazakhstan","Algeria"]

list_to_shuffle = ["Russia","Canada","USA","China","Brazil","Australia","India","Argentina","Kazakhstan","Algeria"]


while len(largestCountries) != 0:

    random.shuffle(list_to_shuffle)
    print(list_to_shuffle)

    random_number = random.randint(0, 9)
    random_country = list_to_shuffle[random_number]

    print(f'What is the ranking of this country {random_country}')
    user_input = int(input('What is you input')) - 1

    if largestCountries[user_input] == random_country:
        print('Correct')
        largestCountries.pop(user_input)

        print(largestCountries)
