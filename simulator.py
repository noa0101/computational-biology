'''
This file contains the simulator which controls the graphics and data presentation
and updates the world every day.
'''

import tkinter as tk
import random
import copy
from world import World
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import numpy as np
from constants import ZERO_CELSIUS


class Simulator:
    # graphical constants
    CELL_SIZE = 42
    NUMBERS_FONT = 16
    TEXT_FONT = 20
    FRAME_TIME = 20  # ms
    TOTAL_DAYS = 365

    def __init__(self):
        self.world = World()

        # these arrays will save the data from every day
        self.pollution = []
        self.temperature = []
        # standard deviation
        self.temp_dev = []
        self.pollute_dev = []

        self.root = tk.Tk()

        # Main window layout
        self.root.title("Earth Simulation")

        # Frame for the matrix (left side)
        self.matrix_frame = tk.Frame(self.root)
        self.matrix_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvas = tk.Canvas(
            self.matrix_frame,
            width=self.CELL_SIZE * self.world.cols,
            height=self.CELL_SIZE * self.world.rows
        )
        self.canvas.pack()
        self.label = tk.Label(self.matrix_frame, text="", font=("Arial", self.TEXT_FONT))
        self.label.pack(pady=10)

        # Frame for the graphs (right side)
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 5))
        self.canvas_graph = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas_graph.draw()
        self.canvas_graph.get_tk_widget().pack()

        self.day = 0

    # runs the simulation
    def run(self):
        self.update_matrix()
        self.root.mainloop()

    # function to format the matrix representation graphically
    def create_matrix(self):
        self.canvas.delete("all")  # Clear the canvas
        matrix = self.world.cells
        for i in range(self.world.rows):
            for j in range(self.world.cols):
                # get location of cell
                x1 = j * self.CELL_SIZE
                y1 = i * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE

                # get color and temperature
                color, number = matrix[i][j].color, round(matrix[i][j].temp - ZERO_CELSIUS)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                self.canvas.create_text(
                    (x1 + x2) // 2, (y1 + y2) // 2,
                    text=str(number),
                    fill="black",
                    font=("Arial", self.NUMBERS_FONT)
                )

    # function to update the world and the presentation accordingly
    def update_matrix(self):
        if self.day > self.TOTAL_DAYS:  # stop after 1 year
            return

        self.create_matrix()
        self.label.config(text=f'Day {self.day}\n\n{self.world.get_stats()}')

        self.world.update()
        self.day += 1

        self.update_graphs()  # update the graphs as well
        self.root.after(self.FRAME_TIME, self.update_matrix)  # update every constant amount of time

    # Function to calculate normalized values, average, and std dev
    @staticmethod
    def calc_normalization(data):
        average = np.mean(data)
        std_dev = np.std(data)
        normalized_data = [(x - average) / std_dev if std_dev != 0 else 0 for x in data]
        return normalized_data

    # Function to update the graphs and display statistics
    def update_graphs(self):
        # Append new data for pollution and temperature
        self.pollution.append(self.world.avrg_pollute)
        self.temp_dev.append(self.world.temp_dev)
        self.temperature.append(self.world.avrg_temp)
        self.pollute_dev.append(self.world.pollute_dev)

        # Calculate normalized data
        normalized_pollution = self.calc_normalization(self.pollution)
        normalized_temperature = self.calc_normalization(self.temperature)
        normalized_temp_dev = self.calc_normalization(self.temp_dev)
        normalized_pollute_dev = self.calc_normalization(self.pollute_dev)

        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()

        # Plot normalized temperature and temperature deviation
        self.ax1.plot(normalized_temperature, label='Normalized Temperature')
        self.ax1.plot(normalized_temp_dev, label='Normalized Temperature Deviation', linestyle='--')
        self.ax1.set_title('Normalized Temperature and Deviation Over Time')
        self.ax1.set_xlabel('Day')
        self.ax1.set_ylabel('Normalized Temperature')
        self.ax1.legend()

        # Plot normalized pollution and pollution deviation
        self.ax2.plot(normalized_pollution, label='Normalized Pollution', color='red')
        self.ax2.plot(normalized_pollute_dev, label='Normalized Pollution Deviation', color='orange', linestyle='--')
        self.ax2.set_title('Normalized Pollution and Deviation Over Time')
        self.ax2.set_xlabel('Day')
        self.ax2.set_ylabel('Normalized Pollution')
        self.ax2.legend()

        # Redraw the graphs
        self.canvas_graph.draw()


if __name__ == "__main__":
    sim = Simulator()
    sim.run()
