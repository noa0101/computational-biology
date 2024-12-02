'''
This file contains a class representing one cell,
which represents a certain region on the earth.
'''

import random
from constants import (POLLUTION_FACTOR, FOREST_CLEANING_FACTOR, CLOUDS_CHANCE, ZERO_CELSIUS, CHANCE_FOR_RAIN,
                       RAIN_EFFECT, HEAT_LOSS_FACTOR, POLLUTION_EFFECT, KILLING_POLLUTION, DAYS_TO_MELT, L, I, F, S, C)


class Cell:
    LAND = L
    SEA = S
    FOREST = F
    ICEBERG = I
    CITY = C
    colors = ((200, 120, 20),  # brown
              (50, 50, 250),  # blue
              (0, 204, 80),  # green
              (255, 255, 255),  # white
              (130, 120, 120))  # grey

    def __init__(self, temp, kind):
        self.kind = kind  # which kind of region
        self.temp = temp  # initial temp - determined randomly according to latitude
        self.wind_down = random.uniform(-1, 1)
        self.wind_right = random.uniform(-1, 1)
        self.clouds = random.random() < CLOUDS_CHANCE

        # set pollution factor of region randomly according to it's kind
        if kind == Cell.CITY:
            self.pollution_factor = POLLUTION_FACTOR*random.random()
        elif kind == Cell.FOREST:
            self.pollution_factor = -1*FOREST_CLEANING_FACTOR*random.random()
        else:
            self.pollution_factor = 0

        self.color = self.get_color(self.colors[kind])
        self.pollute = self.pollution_factor

        if kind == Cell.ICEBERG:
            self.days_above_zero = 0

    # transforms cell to a different kind
    def turn_to(self, kind):
        self.kind = kind
        self.color = self.get_color(self.colors[kind])
        if kind == Cell.CITY:
            self.pollution_factor = POLLUTION_FACTOR*random.random()
        if kind == Cell.FOREST:
            self.pollution_factor = FOREST_CLEANING_FACTOR*random.random()
        else:
            self.pollution_factor = 0

    # returns the color in the right format
    @staticmethod
    def get_color(rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'

    # here are implemented updates of the cell for which only this cell's information is relevant
    def update(self):
        # melt an iceberg
        if self.kind == Cell.ICEBERG and self.temp > ZERO_CELSIUS:
            self.days_above_zero += 1
            if self.days_above_zero > DAYS_TO_MELT:
                self.turn_to(Cell.SEA)

        # make it rain
        if self.clouds:
            if random.random() < CHANCE_FOR_RAIN:
                rain = random.random()  # random amount of rain
                self.temp -= RAIN_EFFECT*rain  # rain lowers temperature

        self.pollute += self.pollution_factor  # pollution is emitted

        self.temp *= HEAT_LOSS_FACTOR
        self.temp += max(0, POLLUTION_EFFECT*self.pollute)  # pollution makes it hotter

        if self.kind == Cell.FOREST and self.pollute > KILLING_POLLUTION:  # if pollution is too high, forests die
            self.turn_to(Cell.LAND)
