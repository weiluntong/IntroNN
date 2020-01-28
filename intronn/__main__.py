import torch
from torch import nn, optim
from torch.nn import functional as F


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

    EPOCHS = 10000

    for _ in range(EPOCHS):
        net.zero_grad()
        output = net(trainset[0])
        loss = F.mse_loss(output, trainset[1])
        loss.backward()
        optimizer.step()
        print(loss)

    print(net(trainset[0]), trainset[1])


if __name__ == "__main__":
    main()
