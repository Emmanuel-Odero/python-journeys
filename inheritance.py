class Car:
    brand = ''
    model = ''
    year = 0
    speed = 0
    mileage = 0

class ElectricalCar(Car):
    battery_capacity = 0

class CEngineCar(Car):
    engine_capacity = 0

car = Car()
car.year = 2020

electrical_car = ElectricalCar
electrical_car.battery_capacity = 2000

c_engine_car = CECar()
c_engine_car.brand = "Toyota"

print(f"Combustion Engine Car brand is: {c_engine_car.brand}")