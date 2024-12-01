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
        self.kind = kind
        self.temp = temp
        self.wind_down = random.uniform(-1, 1)
        self.wind_right = random.uniform(-1, 1)
        self.clouds = random.random() < CLOUDS_CHANCE
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

    def turn_to(self, kind):
        self.kind = kind
        self.color = self.get_color(self.colors[kind])
        if kind == Cell.CITY:
            self.pollution_factor = POLLUTION_FACTOR*random.random()
        if kind == Cell.FOREST:
            self.pollution_factor = FOREST_CLEANING_FACTOR*random.random()
        else:
            self.pollution_factor = 0

    @staticmethod
    def get_color(rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'

    def update(self):
        if self.kind == Cell.ICEBERG and self.temp > ZERO_CELSIUS:
            self.days_above_zero += 1
            if self.days_above_zero > DAYS_TO_MELT:
                self.turn_to(Cell.SEA)

        if self.clouds:
            if random.random() < CHANCE_FOR_RAIN:
                rain = random.random()
                self.temp -= RAIN_EFFECT*rain

        self.pollute += self.pollution_factor

        self.temp *= HEAT_LOSS_FACTOR
        self.temp += max(0, POLLUTION_EFFECT*self.pollute)

        if self.kind == Cell.FOREST and self.pollute > KILLING_POLLUTION:
            self.turn_to(Cell.LAND)
