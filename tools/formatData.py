import csv
import json
import time as time
import numpy as np

def formatD(endgame_dictionary : str, out_location : str):

    print("beginning load")
    with open(endgame_dictionary,'r') as f:
        d = json.load(f)
    print("loaded")

    size = 0
    prevSize = 0
    start = 0

    with open(out_location, 'w') as c:
        mywriter = csv.writer(c)
        for i in d:
            i = eval(i)

            if len(i) != prevSize:
                print(str(len(i)) +': ' + str(time.time() - start))
                start = time.time()
            prevSize = len(i)

            arr = [0] * 101
            for j in i:
                arr[j-1] = 1
            if(d[str(i)][0] == 'W'):
                arr[100] = 1
            mywriter.writerow(arr)
    
    print("finished")
                
def getHalfWin(csv_data : str, out_location: str):
    with open(csv_data, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        with open(out_location, 'w') as out:
            write = csv.writer(out)
            for row in datareader:
                if row[100] == '0':
                    write.writerow(row)
