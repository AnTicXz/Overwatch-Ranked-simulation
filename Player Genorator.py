import numpy as np
import matplotlib.pyplot as plt
import math
mu, sigma , PlayerN = 2350, 700 , 5000 # mean and standard deviation
s = np.random.normal(mu, sigma, PlayerN)


# pandaspd.iloc[idnex]



#s = val.item()
#print(s[1])


#Credit to Numpy documention for plot code
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
#plt.show()


s = np.int_(s)

f = open("PlayerData.txt", "w")
z = 0


# file format needs added
f.write("PlayerID,StartingSR,CurrentSR,Games Played,Games Lost,Games Won")
f.write(" \n")
for item in range(0,PlayerN):
    y = 0
    Pdata = [item , s[z], s[z],0,0,0]
    #print(item)
    #print(s)
    z = z + 1
    for x in range(0,6):
        f.write(str(Pdata[y]))
        if x < 5:
           f.write(',') 
        
        y = y + 1
    #f.write  
    f.write('\n')


f.close()
