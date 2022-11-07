from collections import namedtuple, deque
from random import choice, random

import torch

from Strategy.DQN import DQNUtilities
from Strategy.Strategy import Strategy
from Strategy.DQN.Agent import Agent


class DQNStrategy(Strategy):
    def __init__(self):
        self.agent = Agent(state_size=11, action_size=3, seed=0)
        self.agent.qnetwork_local.load_state_dict(torch.load('Strategy/DQN/checkpoint.pth'))  # load weights from file

    def chose_next_move(self, board):
        state = DQNUtilities.map_to_array(board)
        action = self.agent.act(state)
        return DQNUtilities.map_action_to_direction(board.snake.direction, action)


Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):
    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
