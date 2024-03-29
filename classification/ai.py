from calendar import EPOCH
from cgi import test
import enum
import itertools
import csv
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.tensorboard import SummaryWriter
from sklearn.model_selection import train_test_split
import torchvision
from torchvision import transforms, datasets

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(100, 128)
        self.fc2 = nn.Linear(128, 128)
        """self.fc3 = nn.Linear(64, 128)
        self.fc4 = nn.Linear(128, 256)
        self.fc5 = nn.Linear(256, 128)
        self.fc6 = nn.Linear(128, 64)"""
        self.fc7 = nn.Linear(128, 64)
        self.fc8 = nn.Linear(64, 16)
        self.fc9 = nn.Linear(16, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        """x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.relu(self.fc5(x))
        x = F.relu(self.fc6(x))"""
        x = F.relu(self.fc7(x))
        x = F.relu(self.fc8(x))
        x = self.fc9(x)

        return F.softmax(x, dim = -1) #find what dim means!!!


def testAndRun(data : str):
    """
    This function accepts an endgame dictionary in csv format from formatJsonToCsv to train and test an AI.

    Parameters:
    -----------
    data : str
        location of the binary csv dictionary generated from formatJsonToCsv
    """
    # opening and reading file
    file = open(data)
    csvreader = csv.reader(file)
    train = list(csvreader)
    writer = SummaryWriter()

    #change to float
    train = [[float(s) for s in row] for row in train]

    #create test list for output comparation
    test = []
    for x in range(len(train)):
        test.append(train[x][len(train[x])-1])
        train[x].pop(len(train[x])-1) #pop the output off the train data

    #convert to tensors
    tensor_train = torch.Tensor(train)
    tensor_test = torch.Tensor(test)
    print(tensor_test)

    #separate data set into training and testing
    x_train, x_test, y_train, y_test = train_test_split(tensor_train, tensor_test, test_size=.25, shuffle= True, random_state= 30)
    x_train = x_train.type(torch.FloatTensor)
    x_test = x_test.type(torch.FloatTensor)
    y_train = y_train.type(torch.FloatTensor)
    y_test = y_test.type(torch.FloatTensor)

    batchSize = 1

    net = Net()

    optimizer = optim.AdamW(net.parameters(), lr = .0003)
    EPOCHS = 3

    step = 0

    #train
    for epoch in range(EPOCHS): 
        random = torch.randperm(x_train.shape[0])
        for j in range(x_train.shape[0]):
            i = random[j]
            if y_train[i] == 0:
                y = torch.tensor([1., 0.])
            else:
                y = torch.tensor([0.,1.])
            output = net(x_train[i])
            loss = F.binary_cross_entropy(output, y) 
            writer.add_scalar("loss/train", loss, step)
            step += 1
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(loss)

    correct = 0
    total = 0
    step = 0

    #test
    random = torch.randperm(x_test.shape[0])
    with torch.no_grad():
        for j in range(x_test.shape[0]):
            i = random[j]
            if y_test[i] == 0:
                y = torch.tensor([1., 0.])
            else:
                y = torch.tensor([0.,1.])

            output = net(x_test[i])
            loss = F.binary_cross_entropy(output, y)
            writer.add_scalar("loss/test", loss, step)
            step += 1

            if output[0] > output[1] and y[0] == 1:
                correct += 1
            if output[1] > output[0] and y[1] == 1:
                correct += 1
            total += 1
            #print(y)
        print(loss)

    print("Accuracy: ", correct/total)
