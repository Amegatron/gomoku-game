import torch

class GomokuModel(torch.nn.Module):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.network = torch.nn.Sequential(
            torch.nn.Conv2d(2, 32, 3, 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(32, 128, 3, 1, padding=2),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(128, 256, 3, 1, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(256, 256, 3, 1, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(256, 128, 3, 1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Dropout2d(0.5),
            torch.nn.Flatten(),
            torch.nn.Linear(4000, 1024),
            torch.nn.ReLU(),
            torch.nn.Linear(1024, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, x*y)
        )

        self.soft_max = torch.nn.Softmax(dim=1)

    def forward(self, x, output_mask=None):
        val = self.network(x)
        val = torch.reshape(val, (self.x, self.y))

        if output_mask:
            val *= output_mask

        return torch.nn.Softmax(dim=2)(val)