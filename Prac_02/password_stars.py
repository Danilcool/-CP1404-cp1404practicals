
"""Module docstring"""


# imports
# CONSTANTS

def main():
    get_password()


def get_password():
    user_password = input("Whats your Password?")
    while len(user_password) < 10:
        user_password = input("Whats your Password?")
    else:
        for letter in user_password:
            print("*", end="")


main()
