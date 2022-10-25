class Car():
    color = ""
    model = ""
    speed = 0
    brand = ''
    fuel_tank = 0
    number_of_wheels = 0
    engine_size = 0
    mileage = 0

    first_release = car()
    car.brand = 'Tesla'
    car.model = 'Model S'
    car.engine_size = 396
    car.number_of_wheels = 4
    car.mileage = 0
    car.speed = 200
    car.color = "Whine Red"

    def __init__(self, brand, model):
        self.brand = brand
        model = self.model

    def current_speed(self):
        print ("The speed of the current Tesla Model {self.model} is {self.speed")

car

    