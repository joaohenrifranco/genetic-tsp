from graph import Graph
from population import Population
from genetic import GeneticAlg

FILES_LIST = ["5", "10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "7500", "10000"]
FILE_PATH = "../test_files/points-1000.txt"
POPULATION_SIZE = 50
MUTATION_RATE = 0.015
TOURNAMENT_SIZE = 5
ELITISM = True
MAX_EVOLVE_ITERATIONS = 5000
NUMBER_OF_CONFIRMATIONS = 10

def main():
    for test in FILES_LIST:
        FILE_PATH = f"../test_files/points-{test}.txt"
        # Read from test file
        print(f'Initializing graph from file {FILE_PATH}')
        graph = Graph()
        graph.init_with_coordinates_file(FILE_PATH)

        # Initialize population
        print(f'Initializing population with {POPULATION_SIZE} individuals')
        pop = Population(population_size=POPULATION_SIZE, graph=graph)

        print(f'Inicial guess for path size: {pop.get_fittest().get_distance()}')

        # Evolve population
        algorithm = GeneticAlg(MUTATION_RATE, TOURNAMENT_SIZE, ELITISM, graph.number_of_cities())

        last_result = 0
        result = 0
        confirmations = 0

        for i in range(0, MAX_EVOLVE_ITERATIONS):
            last_result = result
            result = pop.get_fittest().get_distance()
            if last_result == pop.get_fittest().get_distance():
                confirmations += 1
            else:
                confirmations = 0
            if confirmations == 10:
                break
            
            pop = algorithm.evolve_population(pop, graph)
            print(f'Iteration {i} of {MAX_EVOLVE_ITERATIONS}. Result so far: {pop.get_fittest().get_distance()}')
        
        print('Evolving complete!')
        print(f'Final distance: {pop.get_fittest().get_distance()}')
        print(f'Corresponding path: {pop.get_fittest().get_tour_list()}')

main()

    
