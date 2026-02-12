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