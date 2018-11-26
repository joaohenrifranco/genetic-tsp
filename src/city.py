import math

# This class represents a single node in the graph, or "City" in this problem
class City:
    # Initialization with coordinates and an index from the file line
    def __init__(self, x: int, y: int, index: int):
        self.x = x
        self.y = y
        self.index = index

    # Used in console printing
    def __str__(self):
        return str(self.index+1)

    # Used in console printing
    def __repr__(self):
        return str(self.index+1)

    # Euclidian distance to any other city
    def distanceTo(self, other_city: 'City') -> float:
        x_dist = abs(self.x - other_city.x)
        y_dist = abs(self.y - other_city.y)

        return math.sqrt(x_dist * x_dist + y_dist * y_dist)