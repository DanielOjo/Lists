#Daniel Ogunlana
#2d list
#06/01/15



#from table import*

# Name | Kills | Deaths

players= [
    ["k1llmAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]

]

#copy print("{0:<12} {1:<12} {2:<12}".format(players[count][0],players[count][1],players[count][2]))

def table(player):
    for count in range(0,3):
        print("{0:<12} | {1:<12} | {2:<12} |".format(players[count][0],players[count][1],players[count][2]))
        #print("{0:<12".format("-")
        
    
table(players)

