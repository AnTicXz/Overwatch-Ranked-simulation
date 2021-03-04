import pandas as pd
import random 

dataset = pd.read_csv("PlayerData.txt")

def PlayersInRangeFunction(up,down,Run_time):
    for x in range(0, Run_time):
        baseSR = random.randint(400,4600)
        #baseSR = 300
        #print("Base SR for function to run on: " ,baseSR)
        DownSR = baseSR - down
        UpSR = baseSR + up
        
        #print("Players in range " + str(DownSR) + " to " + str(UpSR))
       
        UpRange = dataset.loc[dataset['CurrentSR']<= UpSR]
    
        PlayersInRange = UpRange.loc[dataset['CurrentSR']>= DownSR]
        
        #Total number of players found from this search. 
        Rows = len(PlayersInRange.index)
        #print(Rows , " : Players in range")
        
        while Rows <= 12:
            DownSR = DownSR-25
            UpSR = UpSR+25
            
            #print("\nInvalid player number correction\n")
            #print("Players in range CORRECTOION " + str(DownSR) + " to " + str(UpSR))
            
            UpRange = dataset.loc[dataset['CurrentSR']<= UpSR]
    
            PlayersInRange = UpRange.loc[dataset['CurrentSR']>= DownSR]
            Rows = len(PlayersInRange.index)
        
        
        RandomPlayer = PlayersInRange.sample(n=12)
       
        #From the randomly selected players give the stats of a win to the first 6
        #And give the stats of a win to the second 6
        #Random selection is not needed becasue .sample already does that.
       
        #Game Winner
        RandomPlayer.iloc[0:6,2] += 24
        RandomPlayer.iloc[0:6,3] += 1
        RandomPlayer.iloc[0:6,5] += 1
        
        #Game Loser
        RandomPlayer.iloc[6:12,2] -= 24
        RandomPlayer.iloc[6:12,3] += 1
        RandomPlayer.iloc[6:12,4] += 1
        
        print(RandomPlayer)
        
        dataset['CurrentSR'] = RandomPlayer['CurrentSR'].replace() 
        dataset['CurrentSR'] = dataset['CurrentSR'].fillna(0)
        
        dataset['Games Played'] = RandomPlayer['Games Played'].replace() + dataset['Games Played']
        dataset['Games Played'] = dataset['Games Played'].fillna(0)
        
        dataset['Games Lost'] = RandomPlayer['Games Lost'].replace() + dataset['Games Lost']
        dataset['Games Lost'] = dataset['Games Lost'].fillna(0)
        
        dataset['Games Won'] = RandomPlayer['Games Won'].replace() + dataset['Games Won']
        dataset['Games Won'] = dataset['Games Won'].fillna(0)
    
    
    #print(PlayersInRange)
    
    #print(dataset)
    
    #dataset.drop(dataset.columns[0], axis=1)
    
    dataset.to_csv('Porcd.txt')

    print("fin")
    
PlayersInRangeFunction(100,100,2)
  

"""
  
    take_larger = lambda dataset, RandomPlayer: RandomPlayer if RandomPlayer.any() > dataset.any() else dataset
    
    dataset.combine(RandomPlayer, take_larger , None, True)
    


print(dataset.loc[3])

 
    temp_bla = RandomPlayer[0:6]['CurrentSR'] + 24
    temp_bla = pd.DataFrame(temp_bla)
    list_sr = list(RandomPlayer[0:6]['CurrentSR'])
    temp_bla = list(temp_bla['CurrentSR'])
    RandomPlayer[0:6]['CurrentSR'] = RandomPlayer[0:6]['CurrentSR'].replace(list_sr, temp_bla)
    print(RandomPlayer[0:6]['CurrentSR'])
    

def InvalidPlayernumber(UpSR,DownSR,Rows):
        DownSR = DownSR-25
        UpSR = UpSR+25   
         
        print("\nInvalid player number correction\n")
        print("Players in range CORRECTOION " + str(DownSR) + " to " + str(UpSR))
        
        UpRange = dataset.loc[dataset['CurrentSR']<= UpSR]

        PlayersInRange = UpRange.loc[dataset['CurrentSR']>= DownSR]
                
        Rows = len(PlayersInRange.index)
        #print(Rows , " : Players in range")
        print(PlayersInRange)
        
        if Rows < 12:
            InvalidPlayernumber(UpSR,DownSR,Rows)
        
        return PlayersInRange

# Fuction will generate a random number Bettwen 500 and 4500
# First perimeter is that number + the value, Second perimeter is that number - the value
# fuction will print the players in that SR range
PlayersInRangeFunction(100,110)

dataset = pd.read_csv("PlayerData.txt")
#print(dataset['PlayerID'])

#print(dataset.columns)

#print(dataset['CurrentSR'])

#print(dataset.loc[100]['CurrentSR'])

#Sepcific_player_sr = dataset.loc[89]['CurrentSR']

search_sr = 2000

DownSR = 110

UpSR = 100

DownNumber = search_sr - DownSR

UpNumber = search_sr + UpSR

all_players = dataset.loc[dataset['CurrentSR']<= UpNumber]

all2 = all_players.loc[dataset['CurrentSR']>= DownNumber]

#print(search_sr , "- " + str(DownSR) , " or + " , str(UpSR))
#print(all2)

def stuff(up,down):
    
    baseSR = random.randint(500,4500)
    print(baseSR)
    DownSR = baseSR - down
    UpSR = baseSR + up
    
    print(DownSR)
    print(UpSR)
   
    UpRange = dataset.loc[dataset['CurrentSR']<= UpSR]

    PlayersInRange = UpRange.loc[dataset['CurrentSR']>= DownSR]
    
    print(PlayersInRange)

stuff(100,110)

#print(all2.loc[780]['CurrentSR'])

#print(all2.loc[780])

#print(dataset)
#dataset.head()

x = 0
while x < 1:
   # print(dataset.iloc[random.randint(0,5000),:])
    x = x + 1
    print('-------------')
    
    player = dataset.iloc[1,:]
    
    #print(player[2])
    
    #print(player['CurrentSR'])

    print(dataset.loc[dataset[CurrentSR] == player[2]])

    #1 11 others with sim SR
    
    #put 6v6
    
    # adjust, current sr , games lost/won/played. 
    
#print(dataset.loc[['PlayerID']])
#print(dataset.loc[3, ['PlayerID']] )
"""
