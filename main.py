from tools import formatData
from tools import checkWinRate
from classification import ai
import csv


#formatData.csvToSeparateWinLoss('data/positions_29.csv', 'w.csv', 'l.csv')

#formatData.createTrainingData('w.csv', 'l.csv', '29training.csv', 80000)

ai.testAndRun('data/29training.csv')
