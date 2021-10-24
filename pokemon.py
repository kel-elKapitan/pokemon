# I want a list of the pokemon that have the great effects against more than one type of pokemon. 

# I would like a list of less than 50 pokemon


import pandas as pd
import numpy as pandas
import matplotlib.pyplot as plt
import seaborn as sns





# import the data

raw = pd.read_csv('pokemon.csv')
print(raw.columns)
print(raw.describe())

strong_against = ['against_bug','against_dark', 'against_dragon','against_electric', 'against_fairy', 'against_fight', 'against_fire','against_flying', 'against_ghost', 'against_grass', 'against_ground','against_ice', 'against_normal', 'against_poison', 'against_psychic','against_rock', 'against_steel', 'against_water']

for i in strong_against:
    strongest = raw[raw[i] == 4]

    print('Pokemon strong against ' + i.upper() + ' types')
    print(strongest['name'])
    print('-----------')
    print('\n')





