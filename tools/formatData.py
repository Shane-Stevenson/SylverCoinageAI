import csv
import json
import time as time
import numpy as np

def formatJsonToCsv(endgame_dictionary : str, out_location : str):

    """
    This function accepts an endgame dictionary and transforms it into a .csv file where each position is represented
    by a series of 1's and 0's in which a one at the n'th position represents that this position has n as a valid move, and a zero
    in the n'th position represents that the position does not contain n.

    Parameters:
    -----------
    endgame_dictionary : str
        location of the dictionary generated by EndGameBuilder.py

    out_location : str
        location of the csv file to be created.
    """

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
    """
    This function accepts an endgame dictionary in the binary csv format, and outputs a new csv file in which 50% of the positions
    are winning, and 50% are loosing.

    Parameters:
    -----------
    csv_data : str
        location of the binary csv dictionary generated from formatJsonToCsv

    out_location : str
        location of the csv file to be created.
    """
    count = 0
    with open(csv_data, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        with open(out_location, 'w') as out:
            write = csv.writer(out)
            for row in datareader:
                if row[100] == '0':
                    write.writerow(row)
                    count+=1
                if row[100] == '1' and count >= 1:
                    write.writerow(row)
                    count -= 1

def makeFakeData(out_location : str):
    """
    this function makes a csv file with 5,000 lines with 1,0,0,...,0 and 5,000 lines with 1,1,0,...,1. This function
    is meant to help test an AI and see if it is working properly. If it is, the AI should have 100% accuracy

    Parameters:
    -----------

    out_location : str
        location of the csv file to be created.
    """
    arr1 = [0] * 101
    arr1[0] = 1
    arr1[1] = 1
    arr1[100] = 1
    arr2 =[0] * 101
    arr2[0] = 1
    with open(out_location, 'w') as c:
        mywriter = csv.writer(c)

        for i in range(0, 10000):
            mywriter.writerow(arr1)
            mywriter.writerow(arr2)