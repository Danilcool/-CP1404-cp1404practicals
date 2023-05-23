
NUMBER_SAMPLE_SIZE = 5
numbers_list = []
for number in range(NUMBER_SAMPLE_SIZE):
    numbers_list.append(int(input('Number:')))


average_number = sum(numbers_list) / NUMBER_SAMPLE_SIZE

print(f"The first number is {numbers_list[0]}")
print(f"The last number is {numbers_list[-1]}")
print(f"The smallest number is {min(numbers_list)}")
print(f"The biggest number is {max(numbers_list)}")
print(f"The average number is {average_number}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("What is your name")

if user_name in usernames:
    print('Access granted')
else:
    print('Access denied')
