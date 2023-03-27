
user_input = input("list of:").split(',')


user_list = []
for i in range(len(user_input)):
    user_list.append(int(user_input[i]))

if len(user_list) >= 8:
    count = 0
    for i in range(len(user_list)):
        
        for number in user_list:
            if number == user_list[i]:
                count += 1

    if count > 3:
        print("True")
else:
    print("False")


print(user_list)