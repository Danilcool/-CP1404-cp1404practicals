
#1
with open("name.txt",'w') as file:
    user_name = input('What is your name:')
    file.write(user_name)
#2
with open('name.txt','r') as file:
    name = file.readline()
    print(f'Your name is {name}')
#3
with open("numbers.txt",'r') as file:
    total = 0
    list_of_number = file.readlines()
    for i in range(2):
        total += int(list_of_number[i])
    print(total)

#4
with open("numbers.txt",'r') as file:
    total = 0
    list_of_number = file.readlines()
    for i in list_of_number:
        total += int(i)
    with open("numbers.txt",'a') as file:
        file.write(str(f"\n{total}"))
