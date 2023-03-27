file = open("goals.txt","r")

A_data = []
scores = 0
Russia_scored = 0
overtime = 0
for line in file:
    data = line.split(";")
    player = data[0]
    country = data[1]
    minutes = int(data[2])
    print(player + " from " + country + " scored a goal at the " + str(minutes) + "th minutes")
    scores += 1
    if country == "Russia":
        Russia_scored += 1
    if minutes >= 90:
        overtime += 1




print(f"Total number of scores is {scores}")

print(f"Russia scored {Russia_scored}")

print(overtime)



