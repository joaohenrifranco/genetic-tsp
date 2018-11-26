from random import shuffle
from city import City

class Tour:
    tour = []
    fitness = 0
    distance = 0

    def __init__(self, graph):
        for _ in graph:
            self.tour.append()

    # def __init__(self, tour: list):
    #     self.tour = tour

    def generate_individual(self, graph):
        for city in graph:
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
        
