

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def main():
    user_input = input('Enter a character:')
    while user_input not in alphabet:
        user_input = input('Enter a character:')
    ascii_number = get_ASCII_code(user_input)
    print(f'The ASCII code for g is {ascii_number}')

    user_number = get_valid_number()
    letter = get_letter_from_ASCII_code(user_number)
    print(f"The character for {letter} is ")



def get_valid_number():
    LOWER = 33
    UPPER = 127
    user_number = int(input('Enter a number between 33 and 127:'))

    while user_number < LOWER or user_number > UPPER:
        print('Invalid Number')
        user_number = int(input('Enter a number between 33 and 127:'))
    return user_number

def get_ASCII_code(user_input):
    return ord(user_input)

def get_letter_from_ASCII_code(user_number):
    return chr(user_number)


def get_table():
    for i in range(127):
        print(f"{i} is {get_letter_from_ASCII_code(i)}")

get_table()