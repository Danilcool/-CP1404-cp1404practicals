from silver_service_taxi import SilverServiceTaxi


car = SilverServiceTaxi("Toyota", 20, 2)
car.drive(18)

print(car.__str__())
print(car.get_fare())

