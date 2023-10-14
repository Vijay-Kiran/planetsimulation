import pygame
import math
pygame.init()
# Set the dimensions of the window
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (100, 149, 237)
RED = (188,39,50)
DARK_GREY = (80, 78, 81)
FONT = pygame.font.SysFont("comicsans", 16)



class Planet:
    AU = 149.6e6 * 1000 #astronomical units
    G = 6.67428e-11
    SCALE = 180 / AU #so that 1 AU = 100 pixels approx
    TIMESTEP = 3600*24 #simulating 1 day per tick

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color #RGB tuple for planet's surface color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        #velocities of the planets
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2 #adding width/2 in order to put the planet at center bcuz 0,0 is top left in pygame
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x,y), self.radius)

        #this is to draw the orbits
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x * self.SCALE + WIDTH/2
                y = y * self.SCALE + HEIGHT/2
                updated_points.append((x,y))
            
            pygame.draw.lines(win, self.color, False, updated_points)
        
        #to display the distance, proving its not circular but rather elliptical
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x,y))


    def attraction(self, other): #takes in the planet and other planet as arguments

        #this is to calculate the r value in GMm/ r**2
        other_x, other_y = other.x, other.y
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        #if other planet is sun, simply store the distance
        if other.sun:
            self.distance_to_sun = distance

        #calc of force
        force = self.G * self.mass * other.mass / distance**2

        #use math.atan2 to find tan inverse bcuz tan inverse(y/x) = theta
        theta = math.atan2(distance_y, distance_x)

        # breaking the force into it's x and y components.
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0 #total force in x and y direcns are initialized to 0

        #here, we are calculating the forces exerted by all other planets(as well as sun) on the current planet.
        #Bcuz the sun is not the only body applying force on the planet.
        #for each planet except itself, apply the forces
        #There will be an equilibrium maintained and planet will rotate in an elliptical orbit

        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        #calc of velocities
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        #updating x and y position by using the velocities
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock() #without this, the simulation would run at speed of cpu
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True
    earth = Planet(-1*Planet.AU , 0, 16, BLUE, 5.9742 * 10**24) #-1 multiplied bcuz its put on left of sun
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**22)
    mars.y_vel = 24.007 * 1000

    mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 0.330*10**24)
    mercury.y_vel = 47.4 * 1000

    venus = Planet(-0.732 * Planet.AU, 0, 14, WHITE, 4.8685*10**24)
    venus.y_vel = 35.02 * 1000


    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) #frames per second = 60
        WINDOW.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WINDOW)
        pygame.display.update() #updates all actions which have been performed
    pygame.quit()

main()