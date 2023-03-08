#92.3% of positions are winning in EndgameDictionary.json

import json
import time

def checkWinRate(endgame_dictionary : str):

    print("beginning load")
    with open(endgame_dictionary,'r') as f:
        d = json.load(f)
    print("loaded")

    size = 0
    prevSize = 0
    start = 0


    win = 0
    total = 0
    for i in d:

        if len(eval(i)) != prevSize:
            print(str(len(eval(i))) +': ' + str(time.time() - start))
            start = time.time()
        prevSize = len(eval(i))

        if(d[i][0] == 'W'):
            win+= 1
        total += 1
    
    print(win/total)
