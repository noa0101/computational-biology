ZERO_CELSIUS = 273.15
POLLUTION_FACTOR = 0.3
FOREST_CLEANING_FACTOR = 0.001
CLOUDS_CHANCE = 0.07
CHANCE_FOR_RAIN = 0.2
RAIN_EFFECT = 0.5
POLLUTION_EFFECT = 1
HEAT_LOSS_FACTOR = 1
KILLING_POLLUTION = 2
DAYS_TO_MELT = 3
TEMP_SPREAD = 0.05
POLLUTION_SPREAD = 0.02
WIND_BARRIER = 0.4
POLLUTION_FADE = 0.37

L = 0
S = 1
F = 2
I = 3
C = 4
WORLD_INITIAL_DESIGN = [
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
        [S, S, S, S, C, L, S, S, S, S, S, S, S, S, S, S, S, L, L, L, L, L, F, F, F, F, S, L, L, L, C, L, L, F, F, F, F, F, F, S, S, S, S],
        [S, S, S, S, S, L, L, L, S, S, S, S, S, S, S, S, L, L, L, L, C, L, L, F, F, L, L, S, S, L, L, L, C, L, F, F, F, F, S, S, S, S, S],
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
