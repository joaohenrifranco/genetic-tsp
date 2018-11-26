from random import randint, random
from population import Population
from tour import Tour

class GeneticAlg:
    mutation_rate = 0.0
    tournament_size = 0
    elistism = False
    tour_size = 0

    def __init__(self, mutation_rate: float, tournament_size: int, elistism: bool, tour_size: int):
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elistism = elistism
        self.tour_size = tour_size

    def tournament_selection(self, population: 'Population') -> 'Tour':
        tournament = Population(self.tournament_size, False)

        for i in range(0, self.tournament_size):
            randomId = randint(0,population.get_population_size())
            tournament.save_tour(i, population.get_tour(randomId))
        
        fittest = tournament.get_fittest()

        return fittest

    def mutate(self, tour: 'Tour'):
        for tour_index, city in enumerate(tour):
            if random() < self.mutation_rate:
                second_tour_index = randint(0, tour.get_tour_size())
            
            second_city = tour.get_city(second_tour_index)

            tour.set_city(tour_index, second_city)
            tour.set_city(second_tour_index, city)

    def crossover(self, father: 'Tour', mother: 'Tour') -> 'Tour':
        child = Tour(self.tour_size)
        
        start_pos = randint(0, father.get_tour_size())
        end_pos = randint(0, father.get_tour_size())

        for i in range (0, child.get_tour_size()):
            if (start_pos < end_pos and i > start_pos and i < end_pos):
                child.set_city(i, mother.get_city(i))

            elif (start_pos > end_pos):
                if (not (i < start_pos and i > end_pos)):
                    child.set_city(i, mother.getCity(i))
        
        for i in range (0, mother.get_tour_size()):
            if (not child.contains_city(mother.get_city(i))):
                for j in range (0, child.get_tour_size()):
                    if (child.get_city(j) == None):
                        child.set_city(j, mother.get_city(i))
                        break

        return child

    def evolve_population(self, population: 'Population') -> 'Population':
        new_population = Population(population.get_population_size(), False)
        
        elistism_offset = 0

        if self.elistism:
            new_population.save_tour(0, population.get_fittest())
            elistism_offset = 1
        
        for i in range (elistism_offset, population.get_population_size()):
            mother = self.tournament_selection(population)
            father = self.tournament_selection(population)

            child = self.crossover(father, mother)

            new_population.save_tour(i, child)
        
        for i in range (elistism_offset, population.get_population_size()):
            self.mutate(new_population.get_tour(i))
        
        return new_population