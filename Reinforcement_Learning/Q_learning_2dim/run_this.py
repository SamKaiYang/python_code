from maze_env import Maze
from RL_brain import QLearningTable


def update():
    for episode in range(100):
        # initial observation 環境觀測值(二維位置座標)
        observation = env.reset()

        while True:
            # fresh env 環境刷新
            env.render()

            # RL choose action based on observation 基於觀測值挑選動作 str索引
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward 
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
