from random import shuffle
from city import City
from graph import Graph

class Tour:
    tour = []
    fitness = 0
    distance = 0

    def __init__(self, graph: Graph = None, tour: list = None):
        # Inits Tour with all graph vertices
        if graph != None:
            for _ in range(0, graph.number_of_cities()):
                self.tour.append(None)
            return
        # Inits Tour with list
        if tour != None:
            self.tour = tour
            return

    def generate_individual(self, graph: Graph):
        for city in range(0, graph.number_of_cities()):
            self.set_city(city, city)
        shuffle(self.tour)
    
    def get_tour_size(self):
        return len(self.tour)
    
    def get_city(self, tour_positon: int):
        return self.tour[tour_positon]

    def set_city(self, tour_positon: int, city: City):
        self.fitness = 0
        self.distance = 0
        self.tour[tour_positon] = city

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1/self.get_distance()
        return self.fitness
    
    def get_distance(self):
        if self.distance == 0:
            distance = 0
            for city_index, city in enumerate(self.tour):
                if city_index < len(self.tour):
                    distance += city.distanceTo(self.tour[city_index+1])
        self.distance = distance
        return distance
    
    def contains_city(self, city: City):
        return city in self.tour
        
