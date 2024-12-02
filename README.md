Maman 11 - Question 2:
Cellular automata representing the Earth
Noa Ben Israel
This reopsitory contains this readme file and 4 python files.
In the python files, there is an implementation of a cellular automata that is meant to simulate the earth and specifically the effect of pollution on the global warming and the melting of icebergs.

Explanation about the automata:
  •	The layout is a two-dimensional board of size 23X47, and it is circular - the cell at position (1, 47) is considered to be a neighbour of the cells in positions (1, 1) and (23, 47).
  •	The state of each cell is determined by: 
    o	kind
    o	wind (intensity and direction)
    o	clouds (there of not)
    o	temperature
    o	pollution factor
    o	amount of current pollution
    The amount of possible states is very large and is dependent on the degree of accuracy of numbers in python.
  •	The neighborhood is of type Von Neumann: 4 neighbours (up, down, left, right).
  •	The transition rule is dependent on the wind, temperature and pollution of the adjacent cells, as well as the state of the cell itself. They include temperature and pollution spreading between adjacent cells, drifting of pollution and clouds with the wind, cities emitting pollution, forests cleaning pollution, icebergs melting dew to heat, and forests dying from too much pollution. The transition is also determined by the constants of the system.
    The rule should be much clearer when reading the code Implementing it.

The python files are:
-	constants.py: a file containing the echo system constant values, such as the POLLUTION_FACTOR, CHANCE FOR RAIN, etc.
-	cell.py: a file containing the implementation of a single cell in the automata.
-	world.py: a file containing the implementation of the whole world, containing the cells.
-	simulator.py: this is the main file that runs the simulation and deals with the graphic representation.

To run the simulation on a Windows computer: 
open cmd and go to the folder containing the 4 python files. 
Type the command “python simulator.py”. 
A tkinter window displaying the automata state and graphs with it’s data over time should pop and display the “world” changing every day for 365 days.

The user may change the constants in the file constants.py and run the simulation, thus seeing the effect of each constant on the development of the state.
A very recommended value to change and explore is that of POLLUTION_FACTOR

