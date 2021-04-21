import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Porcd.txt")

print(dataset['Games Played'].sum())

print(dataset['Games Won'].sum())

print(dataset['Games Lost'].sum())



data = dataset.iloc[1]

data.hist(grid = False, bins = 300)



