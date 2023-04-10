"""
Word Occurrences
Estimate: 15 minutes
Actual:   15 minutes
"""

user_email = " "

email_dict = {}

while True:
    user_email = input('Email:')
    user_elements = user_email.split('@')

    if user_email == "":
        break

    if "." in user_elements[0]:
        user_name = user_elements[0].split('.')
        first_name = user_name[0].capitalize()
        last_name = user_name[1].capitalize()
        user_question = input(f'Is your name {first_name, last_name} [Y/N]:')
        if user_question == "Y":
            email_dict[user_email] = f"{first_name} {last_name}"
        else:
            user_name = input("Name:")
            email_dict[user_email] = f"{user_name}"

    else:
        user_name = user_elements[0].capitalize()

        user_question = input(f'Is your name {user_name} [Y/N]:')
        if user_question == "Y":
            email_dict[user_email] = f"{user_name}"
        else:
            user_name = input("Name:")
            email_dict[user_email] = f"{user_name}"

for email, name in email_dict.items():
    print(name, f"({email})")