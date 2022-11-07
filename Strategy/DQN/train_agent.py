import copy

import numpy as np
import torch
from matplotlib import pyplot as plt

import utils
from Controller import compute_next_position, rotate, move_forward, remove_last_position
from utils import losing_next_position
from Model.Board import Board
from Model.Direction import Direction
from Model.Snake import Snake
from Strategy.DQN.Agent import Agent
from Strategy.DQN.DQNUtilities import map_action_to_direction
from View.OutputView.PygameOutputView import PygameOutputView
from DQNUtilities import map_to_array

agent = Agent(state_size=11, action_size=3, seed=0)


def dqn(n_episodes=1000, max_t=1000, eps_start=1.0, eps_end=0.01, eps_decay=0.98, board_size=5):
    """Deep Q-Learning

    Params
    ======
        n_episodes (int): maximum number of training epsiodes
        max_t (int): maximum number of timesteps per episode
        eps_start (float): starting value of epsilon, for epsilon-greedy action_number selection
        eps_end (float): minimum value of epsilon
        eps_decay (float): mutiplicative factor (per episode) for decreasing epsilon

    """
    scores = []  # list containing score from each episode
    # scores_window = deque(maxlen=100)  # last 100 scores
    eps = eps_start
    view = PygameOutputView(board_size)
    for i_episode in range(1, n_episodes + 1):
        state = Board(board_size, Snake((0, 0), Direction.UP))
        score = 0
        eps = max(eps * eps_decay, eps_end)  # decrease the epsilon
        for t in range(max_t):
            t += 1
            # time.sleep(0.05)
            # view.show_board(state)
            action_number = agent.act(map_to_array(state), eps)
            next_state, reward, done = step(copy.deepcopy(state), action_number)
            agent.step(map_to_array(state), action_number, reward, map_to_array(next_state), done)
            snake_size = len(state.snake.position)
            # above step decides whether we will train(learn) the network
            # actor (local_qnetwork) or we will fill the replay buffer
            # if len replay buffer is equal to the batch size then we will
            # train the network or otherwise we will add experience tuple in our
            # replay buffer.
            state = next_state
            if done:
                print('\rEp.{}\t{}.movements\t {}%.exploration\t FinalSize.{}'.format(i_episode, t, int(eps * 100),
                                                                                      snake_size))
                scores.append(snake_size)
                break

    print('Last scores: {}'.format(scores[-100:]))
    torch.save(agent.qnetwork_local.state_dict(), 'checkpoint.pth')

    return scores


def step(board, next_direction_index):
    done = False
    reward = 0
    old_distance_to_food = utils.distance_tuple(board.snake.head, board.food.position)
    # next_direction_index [0, 1, 2]
    next_direction = map_action_to_direction(board.snake.direction, next_direction_index)

    next_position = compute_next_position(board.snake, next_direction.value)
    new_distance_to_food = utils.distance_tuple(next_position, board.food.position)
    if losing_next_position(board, next_position):
        done = True
        reward -= 100

    rotate(board.snake, next_direction)
    move_forward(board.snake, next_position)

    if next_position == board.food.position:
        reward += 10
        board.spawn_food()

    else:
        remove_last_position(board.snake)
        reward += (1, -1)[new_distance_to_food > old_distance_to_food]
    return board, reward, done


scores = dqn()

# plot the scores
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(len(scores)), scores)
plt.ylabel('Score')
plt.xlabel('Epsiode #')
plt.show()

if __name__ == '__train__':
    dqn()
