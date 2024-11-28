import tkinter as tk
import random
class Cell:
    LAND = 0
    SEA = 1
    FOREST = 2
    ICEBERG = 3
    CITY = 4
    #colors = ('brown', 'blue', 'green', 'white', 'grey')
    colors = ((200, 120, 20),
              (50, 50, 250),
              (0, 204, 80),
              (255, 255, 255),
              (130, 120, 120))
    def __init__(self, temp, wind, cloud, kind=SEA, pollution_factor=None):
        self.kind = kind
        self.temp = temp
        self.wind = wind
        self.cloud = cloud
        if kind == Cell.CITY:
            self.pollution_factor = pollution_factor if pollution_factor!=None else random.random()
            #self.color = self.brighten_color(self.pollution_factor * self.colors[kind] + (1-self.pollution_factor)*self.colors[Cell.LAND], 1)
        #else:
        self.color = self.brighten_color(self.colors[kind], 1)
        self.pollution_factor = pollution_factor if kind == Cell.CITY else 0
        self.pollut = self.pollution_factor
        #rgb_color = Cell.colors[kind]
        #self.color = self.brighten_color(rgb_color, 1 + self.pollut)
        self.rain = 0
        if kind == Cell.ICEBERG:
            self.days_above_zero = 0

    @staticmethod
    def brighten_color(rgb, factor):
        """
        Brightens or darkens an RGB color by a factor.
        :param rgb: Tuple (R, G, B)
        :param factor: Float between 0 (black) and 1 (original), >1 brightens
        :return: Hexadecimal color string for tkinter
        """
        r, g, b = rgb
        r = int(min(r * factor, 255))
        g = int(min(g * factor, 255))
        b = int(min(b * factor, 255))
        # Convert back to tkinter-compatible hex color
        return f'#{r:02x}{g:02x}{b:02x}'

    def update(self):
        pass
'''
class World:
    LAND = 0
    SEA = 1
    FOREST = 2
    ICEBERG = 3
    CITY = 4
    def __init__(self):
        self.cells = [[Cell(20, 0, 0, Cell.CITY, 1), Cell(10, 6, 1, Cell.CITY, 0.7)], [Cell(20, 0, 0, Cell.CITY, 0.3), Cell(10, 6, 1, Cell.CITY, 0)]]
'''


class World:
    L = Cell.LAND
    S = Cell.SEA
    F = Cell.FOREST
    I = Cell.ICEBERG
    C = Cell.CITY
    DESIGN = [
            [I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I],
            [S, S, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, S, S, S, S, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, S, S],
            [S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S],
            [S, S, L, L, S, S, S, L, L, L, C, C, S, L, L, L, L, L, S, S, S, S, S, S, L, L, S, S, L, L, L, L, S, S, S, S, L, L, S, S, S, S, S],
            [S, L, L, C, C, L, F, F, S, S, L, C, S, S, L, L, L, S, S, L, L, L, L, S, L, S, S, L, L, L, L, L, L, L, L, L, L, L, L, L, L, L, S],
            [S, L, S, L, C, L, F, F, S, L, S, S, S, S, L, S, S, S, S, L, S, S, F, F, F, F, L, L, L, L, L, L, C, L, L, L, L, L, L, L, L, L, S],
            [S, S, S, L, L, L, L, L, L, L, L, S, S, S, S, S, S, S, S, S, S, S, F, F, F, F, L, L, L, L, L, C, C, C, L, L, L, L, S, S, L, L, S],
            [S, S, F, L, L, L, C, C, L, L, S, S, S, S, S, S, S, S, S, F, F, F, F, F, L, L, L, L, C, F, L, C, C, L, L, L, L, L, L, S, S, L, S],
            [S, S, F, F, L, L, C, C, S, S, S, S, S, S, S, S, S, S, L, L, L, L, L, L, L, L, L, L, F, F, L, L, L, L, L, L, L, L, L, L, S, S, S],
            [S, S, F, F, F, F, L, S, S, S, S, S, S, S, S, S, S, L, L, L, L, L, S, S, L, F, C, C, L, L, C, L, L, L, L, L, L, L, L, S, L, S, S],
            [S, S, S, F, F, L, L, S, S, S, S, S, S, S, S, S, S, L, S, S, L, S, L, L, F, F, F, C, L, C, L, C, L, L, L, L, L, S, S, S, L, S, S],
            [S, S, S, S, L, C, S, S, S, S, S, S, S, S, S, S, S, S, L, L, S, S, S, S, F, F, L, L, L, L, L, L, L, L, F, F, F, F, F, S, L, S, S],
            [S, S, S, S, C, L, S, S, S, S, S, S, S, S, S, S, S, L, L, L, L, L, L, L, L, L, S, L, L, L, C, L, L, F, F, F, F, F, F, S, S, S, S],
            [S, S, S, S, S, L, L, L, S, S, S, S, S, S, S, S, L, L, L, L, C, L, L, L, L, L, L, S, S, L, L, L, C, L, F, F, F, F, S, S, S, S, S],
            [S, S, S, S, S, S, S, L, L, F, F, F, S, S, S, S, L, L, L, C, L, C, L, L, L, S, S, S, S, S, L, L, S, L, L, L, S, S, F, S, S, S, S],
            [S, S, S, S, S, S, S, S, F, F, F, F, F, S, S, S, S, L, L, L, L, L, L, L, L, L, L, S, S, S, L, C, S, S, L, L, S, S, S, S, S, S, S],
            [S, S, S, S, S, S, S, S, F, F, F, F, F, F, S, S, S, S, S, L, L, L, L, L, L, L, S, S, S, S, L, L, S, S, L, S, S, C, L, S, S, S, S],
            [S, S, S, S, S, S, S, S, F, F, F, F, F, F, L, S, S, S, S, S, L, C, L, L, L, L, S, S, S, S, S, L, S, S, S, S, L, C, S, S, S, S, S],
            [S, S, S, S, S, S, S, S, F, F, F, F, F, F, L, S, S, S, S, S, L, L, L, L, L, S, S, S, S, S, S, S, S, S, L, L, S, S, S, S, L, L, S],
            [S, S, S, S, S, S, S, S, S, S, L, C, C, L, S, S, S, S, S, S, L, L, C, C, L, S, L, S, S, S, S, S, S, S, S, L, L, L, S, S, S, L, S],
            [S, S, S, S, S, S, S, S, S, S, F, C, S, S, S, S, S, S, S, S, L, L, L, L, S, L, L, S, S, S, S, S, S, S, S, S, S, S, S, L, S, S, S],
            [S, S, S, S, S, S, S, S, S, S, F, L, S, S, S, S, S, S, S, S, S, L, L, L, S, L, S, S, S, S, S, S, S, S, S, S, S, L, L, L, L, S, S],
            [S, S, S, S, S, S, S, S, S, S, S, L, S, S, S, S, S, S, S, S, S, L, L, S, S, L, S, S, S, S, S, S, S, S, S, L, L, L, L, L, L, S, S],
            [S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, L, S, S, S, S, S, S, S, S, S, S, S, S, S, L, L, L, L, L, L, S],
            [S, S, S, I, I, I, S, I, I, I, I, I, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, I, I, I, I, I, S, S, S, S, S, S, S, S, S, S],
            [S, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, S, S, S, S, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, S, S],
            [I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I, I],
        ]
    def __init__(self, rows = len(DESIGN), cols = len(DESIGN[0])):
        self.rows = rows
        self.cols = cols
        self.cells = self.generate_world()

    def generate_world(self):
        mat = World.DESIGN
        world = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                # Latitude-based temperature distribution (rough approximation)
                latitude = (i / self.rows) * 180 - 90  # Range from -90 to 90 (degrees)
                temp = self.generate_temperature(latitude)

                # Pollution factor based on location
                pollution_factor = self.generate_pollution_factor(i, j)

                # Choose the type of cell based on latitude and other factors
                #kind = self.determine_cell_type(latitude, i, j)
                kind = mat[i][j]

                # Create cell and add it to the world
                row.append(Cell(temp, 0, 0, kind, pollution_factor))
            world.append(row)
        return world

    def update(self):
        cells = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.cells[i][j].update())
            cells.append(row)
        self.cells = cells

    def generate_temperature(self, latitude):
        """Generate temperature based on latitude (basic model)"""
        if latitude < -60 or latitude > 60:
            return random.randint(-30, 0)  # Iceberg/Cold zones (Polar regions)
        elif -60 <= latitude < -30 or 30 < latitude <= 60:
            return random.randint(0, 20)  # Cold temperate zones
        else:
            return random.randint(20, 40)  # Tropical/Equator zones

    def generate_pollution_factor(self, i, j):
        """Generate pollution factor based on location"""
        # Cities have higher pollution
        if random.random() < 0.05:  # 5% chance of a city
            return random.uniform(0.7, 1.5)  # Cities have high pollution
        elif self.is_ocean(i, j):  # Ocean regions have low pollution
            return 0.1
        return random.uniform(0.3, 0.7)  # Forest/land has moderate pollution

    def is_ocean(self, i, j):
        """Returns True if the current cell is part of the ocean"""
        # Sea cells are mostly in the outer rows/columns (like Earth’s oceans)
        return (i < self.rows * 0.1 or i > self.rows * 0.9 or
                j < self.cols * 0.1 or j > self.cols * 0.9)

    def determine_cell_type(self, latitude, i, j):
        """Determine the type of land (sea, forest, iceberg, etc.) based on latitude and location"""
        if self.is_ocean(i, j):
            return Cell.SEA  # Ocean regions
        elif latitude < -60 or latitude > 60:
            return Cell.ICEBERG  # Polar regions (Icebergs)
        elif random.random() < 0.2:  # 20% chance of forest
            return Cell.FOREST
        return Cell.LAND  # Default is land


def create_matrix(canvas, world, cell_size):
    canvas.delete("all")  # Clear the canvas
    matrix = world.cells
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Choose color and number for each cell
            color, number = matrix[i][j].color, matrix[i][j].temp

            # Draw rectangle with color
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            # Write number inside the rectangle
            canvas.create_text(
                (x1 + x2) // 2, (y1 + y2) // 2,
                text=str(number),
                fill="black",
                font=("Arial", 9)
            )


def update_matrix():
    global current_matrix_index
    global world
    world.update()
    create_matrix(canvas, world, cell_size)
    label.config(text=f'Day{current_matrix_index}')



# Corresponding text descriptions
texts = [
    "This is the first matrix!",
    "Here is the second matrix!",
]

world = World()


# Cell size in pixels
cell_size = 24

# Initialize tkinter
root = tk.Tk()
root.title("Matrix Display")

# Create a canvas for the matrix
canvas = tk.Canvas(root, width=cell_size * len(world.cells[0]), height=cell_size * len(world.cells))
canvas.pack()

# Add a label below the matrix
label = tk.Label(root, text=texts[0], font=("Arial", 14))
label.pack(pady=10)

# Show the first matrix initially
current_matrix_index = 0
create_matrix(canvas, world, cell_size)

for i in range(20):
    current_matrix_index+=1
    update_matrix()

# Run the tkinter event loop
root.mainloop()
