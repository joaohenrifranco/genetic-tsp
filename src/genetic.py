from random import randint, random
from population import Population
from tour import Tour

# Class used to organize all genetic mechanics such as mutation and crossover
class GeneticAlg:
    def __init__(self, mutation_rate: float, tournament_size: int, elistism: bool, tour_size: int):
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elistism = elistism
        self.tour_size = tour_size

    # The fittest individual is chosen from a subset
    def tournament_selection(self, population: 'Population', graph) -> 'Tour':
        tournament = Population(self.tournament_size, graph, False)

        for i in range(0, self.tournament_size):
            randomIndex = randint(0,population.get_population_size()-1)
            tournament.save_tour(i, population.get_tour(randomIndex))
        
        fittest = tournament.get_fittest()

        return fittest

    # Introduces random changes to individuals
    # Here, it's just a swap wich guarantees the correctness
    # of the output Tour
    def mutate(self, tour: 'Tour'):
        for tour_index, city in enumerate(tour.get_tour_list()):
            # Only a few should be mutated, preventing chaos
            if random() < self.mutation_rate:
                second_tour_index = randint(0, tour.get_tour_size()-1)
            
                second_city = tour.get_city(second_tour_index)

                tour.set_city(tour_index, second_city)
                tour.set_city(second_tour_index, city)

    # Mix characteristics of a mother and a father into a child
    def crossover(self, father: 'Tour', mother: 'Tour') -> 'Tour':
        child = Tour(self.tour_size)
        
        start_pos = randint(0, father.get_tour_size()-1)
        end_pos = randint(0, father.get_tour_size()-1)

        # Father random subset is pasted into child
        for i in range (0, child.get_tour_size()):
            if (start_pos < end_pos and i > start_pos and i < end_pos):
                child.set_city(i, father.get_city(i))

            elif (start_pos > end_pos):
                if (not (i < start_pos and i > end_pos)):
                    child.set_city(i, father.get_city(i))
        
        # Mother fills the gaps 
        for i in range (0, mother.get_tour_size()):
            if (not child.contains_city(mother.get_city(i))):
                for j in range (0, child.get_tour_size()):
                    if (child.get_city(j) == None):
                        child.set_city(j, mother.get_city(i))
                        break

        return child

    # Function responsible for evolving the population by crossover and mutation
    def evolve_population(self, population: 'Population', graph) -> 'Population':
        new_population = Population(population.get_population_size(), graph, False)
        
        elistism_offset = 0

        # Elitism keeps best individual to next generation
        if self.elistism:
            new_population.save_tour(0, population.get_fittest())
            elistism_offset = 1
        
        # Generate child
        for i in range (elistism_offset, population.get_population_size()):
            mother = self.tournament_selection(population, graph)
            father = self.tournament_selection(population, graph)

            child = self.crossover(father, mother)

            new_population.save_tour(i, child)
        
        # Mutate (by chance)
        for i in range (elistism_offset, population.get_population_size()):
            self.mutate(new_population.get_tour(i))
        
        return new_population