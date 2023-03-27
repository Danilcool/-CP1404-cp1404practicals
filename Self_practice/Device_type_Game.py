#Hardware Quiz - www.101computing.net/hardware-quiz/
import random

score=0
inputDevices = ["mouse","keyboard","webcam","microphone","scanner"]
outputDevices = ["screen","printer","projector","speaker"]
storageDevices = ["Magnetic Hard drive","SSD Hard drive","USB Key","CD Drive","DVD Drive","SD Card Reader"]

#Join both lists together
allDevices = inputDevices + outputDevices + storageDevices


#Select a device randomly from the list of devices

game_on = True

while game_on == True:
    randomDevice = random.choice(allDevices)
    print(randomDevice)
    answer = input(f'Is {randomDevice} (I)nputDevice or (O)utputDevices or (S)torageDevice ?').upper()

    if answer == "I":
        if randomDevice in inputDevices:
            print("True")
            score += 10
        else:
            game_on = False

    elif answer == "O":
        if randomDevice in outputDevices:
            print("True")
            score += 10
        else:
            game_on = False

    elif answer == "S":
        if randomDevice in storageDevices:
            print("True")
            score += 10
        else:
            game_on = False



