from graph import Graph
from population import Population
from genetic import GeneticAlg

FILE_PATH = "../test_files/points-5.txt"
POPULATION_SIZE = 64
MUTATION_RATE = 0.020
TOURNAMENT_SIZE = 4
ELITISM = True
EVOLVE_ITERATIONS = 10

def main():
    # Read from test file
    print(f'Initializing graph from file {FILE_PATH}')
    graph = Graph()
    graph.init_with_coordinates_file(FILE_PATH)

    # Initialize population
    print(f'Initializing population with {POPULATION_SIZE} individuals')
    pop = Population(population_size=POPULATION_SIZE, graph=graph)

    print(f'Inicial guess for path size: {pop.get_fittest().get_distance}')

    # Evolve population
    algorithm = GeneticAlg(MUTATION_RATE, TOURNAMENT_SIZE, ELITISM)

    for i in range(0, EVOLVE_ITERATIONS):
        pop = algorithm.evolve_population(pop)
        print(f'Iteration {i} of {EVOLVE_ITERATIONS}. Result so far: {pop.get_fittest().get_distance}')
    
    print('Evolving complete!')
    print(f'Final distance: {pop.get_fittest().get_distance}')
    print(f'Corresponding path: {pop.get_fittest()}')

main()

    
