from city import City

class Graph:
    visited_cities = []
    cities_file_count = 0

    def add_city(self, city: City):
        return self.visited_cities.append(city)
    
    def get_city(self, index: int):
        return self.visited_cities[index]
    
    def number_of_cities(self):
        return len(self.visited_cities)

    def init_with_coordenates_file(self, input_path: str):
        input_file = open(input_path, "r")
        
        self.cities_file_count = int(input_file.readline())

        for line in input_file:
            coord_list = line.split(" ")
            coord_list[1] = coord_list[1].split("\n")[0]
            
            new_city = City(coord_list[0], coord_list[1])

            self.add_city(new_city)
        
        input_file.close()
