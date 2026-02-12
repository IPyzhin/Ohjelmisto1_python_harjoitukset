class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator on the {self.current_floor}.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator on the {self.current_floor}.")

    def go_to_floor(self, target):
        while self.current_floor != target:
            if target > self.current_floor:
                self.floor_up()
            else:
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        for _ in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, target):
        if elevator_number >= 0 and elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(target)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)