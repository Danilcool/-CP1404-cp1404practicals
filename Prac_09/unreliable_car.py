import random
from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(1,100)
        if random_number < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            print('Car is Broken')

