import math

class City:
    def __init__(self, x: int, y: int, index: int):
        self.x = x
        self.y = y
        self.index = index

    def __str__(self):
        return str(self.index+1)

    def __repr__(self):
        return str(self.index+1)

    def distanceTo(self, other_city: 'City') -> float:
        x_dist = abs(self.x - other_city.x)
        y_dist = abs(self.y - other_city.y)

        return math.sqrt(x_dist * x_dist + y_dist * y_dist)