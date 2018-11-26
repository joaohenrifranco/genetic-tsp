import math

class City:
    x = 0
    y = 0

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    

    def distanceTo(self, other_city: City) -> int:
        x_dist = abs(self.x - other_city.x)
        y_dist = abs(self.y - other_city.y)

        return math.sqrt(x_dist * x_dist + y_dist * y_dist)