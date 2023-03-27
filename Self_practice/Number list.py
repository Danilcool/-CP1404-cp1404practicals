
user_input = input().split(',')

user_list = []

for number in user_input:
    user_list.append(int(number.strip()))


for number in range(len(user_list)):