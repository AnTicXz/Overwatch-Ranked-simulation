import pandas as pd

dataset = pd.read_csv("Porcd.txt")

print(dataset['Games Played'].sum())

print(dataset['Games Won'].sum())

print(dataset['Games Lost'].sum())