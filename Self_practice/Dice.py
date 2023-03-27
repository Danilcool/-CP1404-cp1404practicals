import random

class Dice():

    def __init__(self,numberOfSides=6):
        self.numberOfSides = numberOfSides
        self.value = 1

    def Roll(self):
        self.value= random.randint(1,self.numberOfSides)
        return self.value


dice = Dice()

dice.Roll()
print(dice.value)