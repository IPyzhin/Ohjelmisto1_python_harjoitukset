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

    def drive(self, travelled_time):
        self.travelled_distance += travelled_time * self.current_speed


class Race:
    def __init__(self, name, distance, list_of_cars):
        self.name = name
        self.distance = distance
        self.cars = list_of_cars
        self.finished = False

    def hour_passes(self):
        for car in self.cars:
            car.current_speed = car.current_speed + random.randint(-10, 15)
            if car.current_speed < 0:
                car.current_speed = 0
            elif car.current_speed > car.maximum_speed:
                car.current_speed = car.maximum_speed
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"Car: {car.license_plate} Car max speed{car}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                self.finished = True
                return self.finished
            else:
                return self.finished