import pygame
import sys
import random
import math


class City:
    def __init__(self, name, x_position, y_position, neighbour):
        self.name = name
        self.x_position = x_position
        self.y_position = y_position
        self.neighbour = neighbour
        self.distance = -1
        self.visited = False  

    def __eq__(self, other):
        return other.name == self.name

    def addNeighbour(self, neighbour):
        self.neighbour = neighbour

    def hasNeighbour(self):
        return self.neighbour != ""

    def getDistance(self, neighbour):
        return self.distance

    def getNeighbour(self):
        return self.neighbour
    
    def getPositions(self):
        return self.x_position, self.y_position 

    def getShortestNeighbour(self, cities: list):
        shortest_index = -1
        found = False
        #print(f"Here are the cities: {cities} and length: {len(cities)}")
        for i in range(len(cities)):
            if  cities[i].visited:
                continue
            else:
                delta = (cities[i].x_position- self.x_position)**2 + (cities[i].y_position - self.y_position)**2
                vector_distance = math.sqrt( delta )
                if self.distance == -1 or self.distance > vector_distance:
                    self.distance = vector_distance
                    shortest_index = i
                    found = True
        
        if not found:
            delta = (self.x_position- cities[0].x_position)**2 + (self.y_position - cities[0].y_position)**2
            self.distance = math.sqrt( delta )
            shortest_index = 0

        return shortest_index

             



#  Class stores the shortest path that returns to the original path
class Path:
    def __init__(self, cities, distance):
        self.cities = cities # Array that stores all the cities 
        self.distance = distance # Stores the original distance but in future stores the shortest distance

    def getDistance(self):
        return self.distance

    def getCities(self):
        return self.cities

    def updateTotalDistance(self):
        for i in range(0, len(self.cities)):
            self.distance = self.distance + self.cities[i].distance



# Initialising the pygame
pygame.init()

# All the necessary values required for the pygame screen
width, heigth = 600, 600
screen = pygame.display.set_mode((width, heigth)) 
# The following part is to display the shortest distance in text
pygame.display.set_caption("The Traveling Salesperson Problem")
font_size = 30
font = pygame.font.SysFont(None, font_size)


# The color of the screen and city as well as the size of the city on the screen
background_color = (0, 0, 0) # Black
screen.fill(background_color)
dot_color = (255, 255, 255) # White
dot_radius = 5
line_color = (255, 255, 255) # White
line_width = 1
text_color = (255, 255, 255) # Black



# This is the number of cities that is specified from our input
num_cities = int(sys.argv[1])
random_x_positions = random.sample( range(0, width), num_cities) # Array to store UNIQUE random x positions for the cities
random_y_positions = random.sample( range(15, heigth), num_cities) # Array to store UNIQUE random y positions for the cities
cities = [] # Array that stores all the cities
for i in range(0, num_cities):
    cities.append( City(f"City{i}", random_x_positions[i], random_y_positions[i], "") ) # Appeding new instances in the cities list




# Now we use Hamiltonian path finging to find the shortest path
full_distance = 0 # Contains the full distance of the path
#print(num_cities)
visited = []   # Is used as a dummy variable to ensure we visit all nodes
index = 0  # Specifies the index in which we are currently at
while len(visited) < num_cities:
    visited.append(1)
    cities[index].visited = True
    temp_index = cities[index].getShortestNeighbour(cities)
    cities[index].addNeighbour(cities[temp_index])
    index = temp_index
    #print(index)




    #print(f"index: {i}")
    # We need to account for the last city of the graph which must go to the original city
    #if i == num_cities-1:
    #    print("Here")
    #    delta = (cities[i].x_position- cities[0].x_position)**2 + (cities[i].y_position - cities[0].y_position)**2
    #    distance = math.sqrt( delta )
    #    cities[i].addNeighbour( cities[0], distance ) # Stores the distance between the first nodes
    #    continue

    #shortest_distance = 0  # Stores the shortest distance from a neighbour
    #found = False  # Shows whether or not the current city has a neighbour or not
    #for j in range( 0, num_cities):
    #    if i == j or j == 0:
    #        #print(cities[i].hasNeighbour())
    #        #print(f"Here with index: {i} and jay equals {j}")
    #        continue
    #    elif  not found:
    #        delta = (cities[i].x_position- cities[j].x_position)**2 + (cities[i].y_position - cities[j].y_position)**2
    #        distance = math.sqrt( delta )
    #        shortest_distance = distance
    #        cities[i].addNeighbour( cities[j], distance ) # Stores the distance between the first nodes
    #        found = True
    #        continue#

        # If the above cases are not met then we check if there is another shortest next node
    #    delta = (cities[i].x_position- cities[j].x_position)**2 + (cities[i].y_position - cities[j].y_position)**2
    #    distance = math.sqrt( delta )
    #    if distance < shortest_distance:
    #        shortest_distance = distance
    #        cities[i].addNeighbour( cities[j], distance ) # Stores the distance between the first nodes
    #        continue

        

    #if i == num_cities-1:
    #    delta = (cities[i].x_position- cities[0].x_position)**2 + (cities[i].y_position - cities[0].y_position)**2
    #    distance = math.sqrt( delta )
    #    cities[i].addNeighbour( cities[0], distance ) # Last city has to go to the initial city
    #    full_distance = full_distance + distance
    #else:
    #    delta = (cities[i].x_position- cities[i+1].x_position)**2 + (cities[i].y_position - cities[i+1].y_position)**2
    #    distance = math.sqrt( delta )        
    #    cities[i].addNeighbour( cities[i+1], distance ) # Last city has to go to the initial city
    #    full_distance = full_distance + distance


path = Path(cities, full_distance) # Initial path
path.updateTotalDistance()



# The running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            for idx, city in enumerate(cities):
                if idx == 0:
                    pygame.draw.circle(screen, (0, 0, 255), city.getPositions(), dot_radius) # initial city with different color
                    continue
                pygame.draw.circle(screen, dot_color, city.getPositions(), dot_radius) # Draw all the cities
            for idx,city in enumerate(path.getCities()):
                if idx == 0:
                    pygame.draw.line(screen, (0, 0, 255), city.getPositions(), city.getNeighbour().getPositions(), line_width) # initial line with different color
                else:
                    #print(idx)
                    pygame.draw.line(screen, line_color, city.getPositions(), city.getNeighbour().getPositions(), line_width) # draw the lines from city to city
                
                
                text_distance = round(path.getDistance(), 1)
                text_surface = font.render(f"Shortest Distance: {text_distance}", True, text_color)
                text_rect = text_surface.get_rect(center=(width//2, 10))
                screen.blit(text_surface, text_rect) # Draw the text that specifies the total distance

    # Updates the display of the screen
    pygame.display.flip()





#Free anything that needs to be freed
pygame.quit()
sys.exit()