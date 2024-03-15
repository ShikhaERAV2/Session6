# import the necessary packages.
from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
#!pip install torchsummary
from torchsummary import summary
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1) # i = 28 o=28
        self.batch1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 16, 3, stride=2, padding=1) # i = 28 o=14
        self.batch2 = nn.BatchNorm2d(16)
        self.mp1 = nn.MaxPool2d(2, 2) # i = 14 o=7
        self.dropout = nn.Dropout(0.05)


        self.conv3 = nn.Conv2d(16, 16, 3, padding=0) # i = 7 o=5
        self.batch3 = nn.BatchNorm2d(16)
        self.conv4 = nn.Conv2d(16, 32, 3, stride=1, padding=0) # i = 5 o=3
        self.batch4 = nn.BatchNorm2d(32)
        self.conv5 = nn.Conv2d(32, 32, 3, stride=1, padding=1) # i = 3 o=3
        self.batch5 = nn.BatchNorm2d(32)
        self.avgpool =  nn.AvgPool2d(3)# i = 3 o=1
        self.fc = nn.Linear(32, 10)

    def forward(self, x):
        x = self.batch1(F.relu(self.conv1(x)))
        x = self.batch2(F.relu(self.conv2(x)))
        x = self.mp1(x)
        x = self.dropout(x)

        x = self.batch3(F.relu(self.conv3(x)))
        x = self.batch4(F.relu(self.conv4(x)))
        x = self.batch5(F.relu(self.conv5(x)))
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        x = F.log_softmax(x, dim=1)
        return x