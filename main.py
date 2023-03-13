from tools import formatData
from tools import checkWinRate
from classification import ai
import csv

#formatData.formatJsonToCsv('unformattedData/EndgameDictionary.json', 'data/positions_30.csv')

# formatData.getHalfWin('data/positions_30.csv', 'data/positions_30_half.csv')

# checkWinRate.checkWinRateCsv('data/positions_30_half.csv')

ai.testAndRun('data/fake.csv')
