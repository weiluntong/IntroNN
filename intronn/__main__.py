import torch
from torch import nn, optim
from torch.nn import functional as F
import numpy as np


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc1(x))


def main():
    trainset = [
        torch.Tensor(
            [[3, 1.5], [2, 1], [4, 1.5], [3, 1], [3.5, 0.5], [2, 0.5], [5.5, 1], [1, 1]]
        ),
        torch.Tensor([[1], [0], [1], [0], [1], [0], [1], [0]]),
    ]
    testset = [
        torch.Tensor([[4.5, 1],]),
    ]
    net = Net()

    optimizer = optim.Adam(net.parameters(), lr=0.001)

    #set array used for random permutation
    perm = np.arange(trainset[0].shape[0])

    EPOCHS = 10000

    #network results at the beginning
    initial = net(trainset[0])

    for _ in range(EPOCHS):
        optimizer.zero_grad()
        output = net(trainset[0])
        loss = F.mse_loss(output, trainset[1])
        loss.backward()
        optimizer.step()
        if _ % 1000 == 0:
            print(loss.item())

        #Randomly permute the training set - reassign based on random indexing
        np.random.shuffle(perm)
        trainset[0][np.arange(perm.shape[0])] = trainset[0][perm] 
        trainset[1][np.arange(perm.shape[0])] = trainset[1][perm]
        
        
    print(f"Initial predctions from network: {initial}")
    print(f"Final predictions from network: {net(trainset[0])}")
    print(f"Actual labels: {trainset[1]}")


if __name__ == "__main__":
    main()
