from cell import Cell
import random
import copy
from constants import WORLD_INITIAL_DESIGN, ZERO_CELSIUS, TEMP_SPREAD, POLLUTION_SPREAD, WIND_BARRIER, POLLUTION_FADE
import numpy as np


class List(list):
    def __getitem__(self, index):
        if index >= len(self):  # Handle index greater than size
            index %= len(self)
        return super().__getitem__(index)


class World:
    def __init__(self):
        self.rows = len(WORLD_INITIAL_DESIGN)
        self.cols = len(WORLD_INITIAL_DESIGN[0])
        self.cells = List()
        for i in range(self.rows):
            row = List()
            for j in range(self.cols):
                latitude = (i / self.rows) * 180 - 90  # Range from -90 to 90 (degrees)
                temp = self.generate_temperature(latitude)
                kind = WORLD_INITIAL_DESIGN[i][j]
                row.append(Cell(temp, kind))
            self.cells.append(row)

        self.initial_amounts = None
        self.initial_temp = None
        self.avrg_temp = None
        self.avrg_pollute = None
        # standard deviations
        self.temp_dev = None
        self.pollute_dev = None
        self.get_stats()

    def get_stats(self):
        amounts = [0, 0, 0, 0, 0]
        temps = []
        pollutes = []

        for i in range(self.rows):
            for j in range(self.cols):
                amounts[self.cells[i][j].kind] += 1
                temps.append(self.cells[i][j].temp)
                pollutes.append(self.cells[i][j].pollute)

        self.avrg_temp = np.mean(temps) - ZERO_CELSIUS
        self.temp_dev = np.std(temps)
        self.avrg_pollute = np.mean(pollutes)
        self.pollute_dev = np.std(pollutes)

        if self.initial_amounts is None:
            self.initial_amounts = amounts
            self.initial_temp = self.avrg_temp

        return (f'Amount of icebergs: {amounts[Cell.ICEBERG]} (initial: {self.initial_amounts[Cell.ICEBERG]})\n'
                f'Amount of forests: {amounts[Cell.FOREST]} (initial: {self.initial_amounts[Cell.FOREST]})\n\n'
                f'Average temperature: {self.avrg_temp:.1f} (initial: {self.initial_temp:.1f})\n'
                f'Average pollution: {self.avrg_pollute:.3f}')

    def updated_cell(self, i, j):
        cell = copy.copy(self.cells[i][j])
        cell.temp = ((1-4*TEMP_SPREAD)*cell.temp + TEMP_SPREAD *
                     (self.cells[i+1][j].temp+self.cells[i][j+1].temp+self.cells[i-1][j].temp+self.cells[i][j-1].temp))
        cell.pollute = ((1-4*POLLUTION_SPREAD)*cell.pollute + POLLUTION_FADE *
                        (self.cells[i + 1][j].pollute + self.cells[i][j + 1].pollute + self.cells[i - 1][j].pollute + self.cells[i][j - 1].pollute))

        if abs(cell.wind_down) + abs(cell.wind_right) > 2*WIND_BARRIER:
            cell.clouds = False

        if self.cells[i+1][j].wind_down < -1*WIND_BARRIER:
            cell.pollute += POLLUTION_SPREAD*self.cells[i+1][j].pollute
            cell.wind_down = 0.5*(cell.wind_down + self.cells[i+1][j].wind_down)
            cell.clouds |= self.cells[i+1][j].clouds

        if self.cells[i-1][j].wind_down > WIND_BARRIER:
            cell.pollute += POLLUTION_SPREAD*self.cells[i-1][j].pollute
            cell.wind_down = 0.5*(cell.wind_down + self.cells[i-1][j].wind_down)
            cell.clouds |= self.cells[i-1][j].clouds

        if self.cells[i][j+1].wind_right < -1*WIND_BARRIER:
            cell.pollute += POLLUTION_SPREAD*self.cells[i][j+1].pollute
            cell.wind_right = 0.5*(cell.wind_down + self.cells[i][j+1].wind_right)
            cell.clouds |= self.cells[i][j+1].clouds

        if self.cells[i][j-1].wind_right > WIND_BARRIER:
            cell.pollute += POLLUTION_SPREAD*self.cells[i][j-1].pollute
            cell.wind_right = 0.5*(cell.wind_down + self.cells[i][j-1].wind_right)
            cell.clouds |= self.cells[i][j-1].clouds

        if self.cells[i+1][j].wind_down < 0:
            cell.wind_down = 0.5*(cell.wind_down + self.cells[i+1][j].wind_down)

        if self.cells[i-1][j].wind_down > 0:
            cell.wind_down = 0.5*(cell.wind_down + self.cells[i-1][j].wind_down)

        if self.cells[i][j+1].wind_right < 0:
            cell.wind_right = 0.5*(cell.wind_down + self.cells[i][j+1].wind_right)

        if self.cells[i][j-1].wind_right > 0:
            cell.wind_right = 0.5*(cell.wind_down + self.cells[i][j-1].wind_right)

        cell.pollute *= POLLUTION_FADE

        cell.update()
        return cell

    def update(self):
        cells = List()
        for i in range(self.rows):
            row = List()
            for j in range(self.cols):
                row.append(self.updated_cell(i, j))
            cells.append(row)
        self.cells = cells

    def generate_temperature(self, latitude):
        if latitude < -60 or latitude > 60:
            return random.randint(-30, 0) + 273  # Iceberg/Cold zones (Polar regions)
        elif -60 <= latitude < -30 or 30 < latitude <= 60:
            return random.randint(0, 20) + 273  # Cold temperate zones
        else:
            return random.randint(20, 40) + 273  # Tropical/Equator zones

