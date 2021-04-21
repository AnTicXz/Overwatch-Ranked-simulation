import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Porcd.txt")

print(dataset['Games Played'].sum())

print(dataset['Games Won'].sum())

print(dataset['Games Lost'].sum())



t1 = list(dataset["CurrentSR"])
t2 = list(dataset["StartingSR"])

plt.hist(t2, 500 ,facecolor='red',alpha=1, label ="Starting SR")
plt.hist(t1, 500,facecolor='black',alpha=1, label = "Current SR")
plt.xlabel("Players SR")
plt.ylabel("Number of players")
plt.legend(loc="upper right")


#plt.savefig('filename.png', dpi=300)