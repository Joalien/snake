import torch
import torch.nn as nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    """ Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_unit=100, fc2_unit=100, fc3_unit=100):
        """
        Initialize parameters and build model.
        Params
        =======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_unit (int): Number of nodes in first hidden layer
            fc2_unit (int): Number of nodes in second hidden layer
            fc2_unit (int): Number of nodes in third hidden layer
        """
        super(QNetwork, self).__init__()  # calls __init__ method of nn.Module class
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_unit)
        self.fc2 = nn.Linear(fc1_unit, fc2_unit)
        self.fc3 = nn.Linear(fc2_unit, fc3_unit)
        self.fc4 = nn.Linear(fc3_unit, action_size)

    def forward(self, state):
        """
        Build a network that maps state -> action values.
        """
        state = F.relu(self.fc1(state))
        state = F.relu(self.fc2(state))
        state = F.relu(self.fc3(state))
        return self.fc4(state)
