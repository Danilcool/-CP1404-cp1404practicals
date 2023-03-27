import random



number = []

while len(number) != 6:
    random_number = random.randint(1,50)
    if random_number not in number:
        number.append(random_number)
number.sort()
print(number)