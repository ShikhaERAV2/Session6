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
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3)
        self.batch1 = nn.BatchNorm2d(8)
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3)
        self.conv3 = nn.Conv2d(16, 32, kernel_size=3)
        self.dropout = nn.Dropout(0.05)
        self.batch2 = nn.BatchNorm2d(32)
        self.fc1 = nn.Linear(3200, 10)
        
    def forward(self, x):
        x = F.relu(self.batch1(self.conv1(x)), 2) 
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        x = self.batch2(F.relu(self.dropout(self.conv3(x)), 2)) 
        x = x.view(-1, 3200) 
        x = F.relu(self.fc1(x))
        return F.log_softmax(x)