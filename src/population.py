from tour import Tour

class Population:
    
    tours = []

    def __init__(self, population_size: int, initialise: bool):
        for _ in range(0, population_size):
            self.tours.append(Tour())
        
        if initialise:
            for tour in self.tours:
                tour.generate_individual()
    
    def get_tour(self, tour_index: int) -> Tour:
        return self.tours[tour_index]
    
    def get_fittest(self) -> Tour:
        fittest = self.tours[0]

        for tour in self.tours:
            if tour.get_fitness() > fittest:
                fittest = tour
        
        return tour
    
    def get_population_size(self) -> int:
        return len(self.tours)

    def save_tour(self, index: int, tour: Tour):
        self.tours[index] = tour