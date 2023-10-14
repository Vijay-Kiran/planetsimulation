# planetsimulation
This project uses pygame library and math library in python in order to simulate the revolution of the planets around the Sun.
It creates a basic planetary system with the Sun and several planets and simulates their orbits and positions over time.

![](Screenshot%202023-10-15%20002131.png)

The steps are:-
1) Import Pygame and initialize it.

2) Define the dimensions of the simulation window and create the window.

3) Define some color constants and a font for text rendering.

4) Create a Planet class to represent planets in the simulation. Each Planet object has attributes such as its position, radius, color, mass, velocities, and methods to calculate attraction forces and update positions.

5) Inside the main function:
  Set up the simulation by creating instances of the Planet class for the Sun and several planets.
  Define their initial positions, velocities, and other properties.
  Add these planets to the planets list.
  
6) The main game loop:
  Keeps the simulation running.
  Updates the positions and velocities of all the planets in the planets list based on gravitational attraction.
  Draws the planets and their orbits on the screen.
  Handles the Pygame quit event to exit the loop when you close the window.
  
7) Pygame continuously updates the display to create an animation of the planets' motion.


   This code essentially simulates the motion of celestial bodies in space, taking into account gravitational forces and providing a visual representation of the planets' orbits around the Sun. It's a simple yet educational simulation of planetary motion.
