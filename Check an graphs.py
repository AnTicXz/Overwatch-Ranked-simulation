import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Porcd.txt")

print(dataset['Games Played'].sum())

print(dataset['Games Won'].sum())

print(dataset['Games Lost'].sum())



t1 = list(dataset["CurrentSR"])
t2 = list(dataset["StartingSR"])

"""
plt.hist(t2, 250 ,facecolor='red',alpha=1, label ="Starting SR")
plt.hist(t1, 250,facecolor='black',alpha=1, label = "Current SR")
plt.xlabel("Players SR")
plt.ylabel("Number of players")
plt.legend(loc="upper right")

"""




t3 = [None] *5000

num = 0
for x in t2:
    t3[num] = x - t1[num]
    num = num + 1
    
plt.scatter(t3,t2, alpha = 0.25, s=3.5, color="orange")
plt.xlabel("SR Delta")
plt.ylabel("Starting SR")



plt.savefig('filen6ame.png', dpi=300)