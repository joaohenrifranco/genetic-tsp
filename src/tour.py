from random import shuffle
from city import City
from graph import Graph

# A individual in the population. Its a single candidade path for the 
# traveling salesman in the graph.
class Tour:
    # Initialize the tour with a array allocation
    def __init__(self, tour_size):
        self.tour = []
        self.fitness = 0
        self.distance = 0

        for i in range(0, tour_size):
            self.tour.append(None)

    # Creates a random tour
    def generate_individual(self, graph: 'Graph'):
        # Add all graph nodes to the tour
        for city_index in range(0, graph.number_of_cities()):
            self.set_city(city_index, graph.get_city(city_index))
        # Shuffle them to make a random order
        shuffle(self.tour)
    
    # Returns current tour array lenght (not distance)
    def get_tour_size(self) -> int:
        return len(self.tour)
    
    # Returns city in corresponding tour index
    def get_city(self, index: int) -> 'City':
        return self.tour[index]

    # Puts city in corresponding tour index
    def set_city(self, index: int, city: 'City'):
        self.tour[index] = city
        # Altering a tour means need for recomputing fitness and distance
        self.fitness = 0
        self.distance = 0

    # Compute when necessary and return tour fitness
    def get_fitness(self) -> float:
        if self.fitness == 0:
            self.fitness = 1/self.get_distance()
        return self.fitness
    
    # Computes when necessary and returns tour total distance
    def get_distance(self) -> float:
        if self.distance == 0:
            distance = 0
            for city_index, city in enumerate(self.tour):
                if city_index + 1 < len(self.tour):
                    distance += city.distanceTo(self.tour[city_index+1])
                else:
                    distance += city.distanceTo(self.tour[0])
            self.distance = distance
        return self.distance
    
    # Checks if tour contains a city
    def contains_city(self, city: 'City') -> bool:
        return city in self.tour
    
    def get_tour_list(self) -> list:
        return self.tour
        
