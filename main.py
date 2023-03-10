from tools import formatData
from tools import checkWinRate
from classification import ai
import csv

#formatData.formatD('unformattedData/EndgameDictionary.json', 'data/positions_30.csv')

# formatData.getHalfWin('data/positions_small.csv', 'out.csv')

# checkWinRate.checkWinRateCsv('out.csv')
ai.testAndRun('out.csv')
