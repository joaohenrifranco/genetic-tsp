class Graph:
    visited_cities = []

    def addCity(self, city):
        return self.visited_cities.append(city)
    
    def getCity(self, index):
        return self.visited_cities[index]
    
    def number_of_cities(self):
        return len(self.visited_cities)

    def init_with_coordenates_file(self, input_path):
        input_file = open(input_path, "r")
        
        for line in input_file:
            coord_list = line.split(" ")
            coord_list[1] = coord_list[1].split("\n")[0]
            
            new_city = city(coord_list[0], coord_list[1])
        
        input_file.close()
