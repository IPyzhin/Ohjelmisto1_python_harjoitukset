import random


class Car:
    def __init__(self, license_plate, maximum_speed,
                 current_speed=0,
                 travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, travelled_time: float):
        self.travelled_distance += travelled_time * self.current_speed


def race(cars):
    while max(car.travelled_distance for car in cars) < 10000:
            for car in cars:
                speed_change = random.randint(-10, 15)
                car.accelerate(speed_change)
                car.drive(1)
    return cars


car1 = Car("ABC-123", 142)
car2 = Car("CBD-127", 170)
car3 = Car("KPK-128", 190)
racecars = [car1, car2, car3]
race(racecars)