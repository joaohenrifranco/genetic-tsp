from city import City

class Graph:
    def __init__(self):
        self.cities_to_visit = []
        self.cities_file_count = 0

    # Add city to the array
    def add_city(self, city: 'City'):
        self.cities_to_visit.append(city)
    
    # Returns city from cities_to_visit array index
    def get_city(self, index: int) -> 'City':
        return self.cities_to_visit[index]
    
    # Returns total number of cities
    def number_of_cities(self) -> int:
        return len(self.cities_to_visit)

    # Reads a file with a first line with umber of vertices
    # and all followig lines with x and y coodinates separated
    # by space
    def init_with_coordinates_file(self, input_path: str):
        input_file = open(input_path, "r")
        
        self.cities_file_count = int(input_file.readline())

        for index, line in enumerate(input_file):
            coord_list = line.split(" ")
            coord_list[1] = coord_list[1].split("\n")[0]
            
            new_city = City(int(coord_list[0]), int(coord_list[1]), index)

            self.add_city(new_city)
        
        input_file.close()
