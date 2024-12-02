'''
This file contains constants relevant to the cellular automata
'''

# constants of the ecosystem
POLLUTION_FACTOR = 0.3  # recommended values to explore: 0.3 (stable), 0.5 (shows significant harm)
ZERO_CELSIUS = 273.15  # the data is saved in the code is in kelvin, but presented in kelvin
FOREST_CLEANING_FACTOR = 0.001  # forests clean the air from pollution
CLOUDS_CHANCE = 0.07  # every cell is initialized to have cloud randomly by this chance
CHANCE_FOR_RAIN = 0.2  # every day clouds have this chance of raining
RAIN_EFFECT = 0.6   # rain lowers temperature
POLLUTION_EFFECT = 1  # how much a certain amount of pollution affect the temp
HEAT_LOSS_FACTOR = 1  # how much heat is lost every day
KILLING_POLLUTION = 0.25  # the amount of pollution required to kill a forest
DAYS_TO_MELT = 3  # amount of days above 0C needed for an iceberg to melt
TEMP_SPREAD = 0.05  # how much temp spreads between neighboring regions every day
POLLUTION_SPREAD = 0.02  # how much pollution spreads between neighboring regions every day
WIND_BARRIER = 0.4  # how much wind is needed to move clouds and pollution
POLLUTION_FADE = 0.37  # a factor by which the pollution fades every day

# constants representing different types of regions
L = 0  # land
S = 1  # sea
F = 2  # forest
I = 3  # iceberg
C = 4  # city
# starting state of the world
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
