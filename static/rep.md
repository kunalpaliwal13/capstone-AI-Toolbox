<br><h1>Understanding Reinforcement Learning Policies in Python</h1>

<h1>Table of Contents</h1>
- Introduction to Reinforcement Learning (RL)
- What Are RL Policies?
- Why Use RL for Decision-Making?
- Installation and Setup
- Implementing RL Policies
- Evaluating RL Models
- Conclusion

<h1>Introduction to Reinforcement Learning (RL)</h1>
Reinforcement Learning (RL) is a machine learning paradigm where an agent learns by interacting with an environment to maximize cumulative rewards. It is widely used in robotics, game AI, and autonomous systems.
The ReinforcementLearning-Policy repository provides implementations of RL policies, demonstrating how agents learn optimal actions over time.

<h1>What Are RL Policies?</h1>
An RL policy defines how an agent chooses actions based on the current state. Policies can be:
- <strong>Deterministic:</strong> The same action is chosen every time for a given state
- <strong>Stochastic:</strong> Actions are chosen based on probability distributions
The repository covers value-based and policy-based approaches to decision-making in RL.

<h1>Why Use RL for Decision-Making?</h1>
Reinforcement Learning is ideal for:
- Sequential decision-making (e.g., self-driving cars, robotics, trading bots)
- Learning from interactions without explicit supervision
- Handling uncertain environments where rules are not predefined
The repository demonstrates how RL can be applied in various scenarios to improve decision-making.

<h1>Installation and Setup</h1>
To run the implementations, install the required dependencies:

<h2>i. Clone the repository:</h2>
<pre>
git clone https://github.com/VITB-Tigers/ReinforcementLearning-Policy
</pre>

<h2>ii. Create and activate a virtual environment (recommended). If using Conda:</h2>
<pre>
conda create -n env_name python==3.11.0 -y
conda activate env_name
</pre>

<h2>iii. Install dependencies:</h2>
<pre>
pip install -r requirements.txt
</pre>

<h2>Running the Implementation:</h2>
<pre>
i. Open a terminal in the project directory
ii. Run the script:
python dqn.py

iii. Adjust training episodes (optional):
main(episode_number=1000)
</pre>
Note: The trained model's weights are periodically saved as .h5 files in the current directory.

<h1>Implementing RL Policies</h1>
The repository includes an example of Deep Q-Network (DQN) implementation:<br>
![alt text](/static/image-10.png)<br>

<pre>
import numpy as np
import tensorflow as tf
from collections import deque

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0   # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = self._build_model()
        
    def _build_model(self):
        # Neural Net for Deep Q Learning
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(24, input_dim=self.state_size, activation='relu'),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=0.001))
        return model
</pre>

<h1>Evaluating RL Models</h1>
Key evaluation metrics for RL policies include:<br>

![alt text](/static/image-11.png)<br>
- <strong>Episode Rewards:</strong> Total rewards accumulated per episode
- <strong>Convergence Rate:</strong> How quickly the policy learns optimal behavior
- <strong>Exploration vs Exploitation:</strong> Balance between trying new actions and using known good actions

<pre>
def evaluate_policy(agent, env, n_episodes=100):
    total_rewards = []
    for episode in range(n_episodes):
        state = env.reset()
        episode_reward = 0
        done = False
        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            episode_reward += reward
            state = next_state
        total_rewards.append(episode_reward)
    return np.mean(total_rewards)
</pre>

<h1>Conclusion</h1>
The ReinforcementLearning-Policy repository provides a practical introduction to RL policies and decision-making strategies. By exploring this repo, you can:
- Understand the fundamentals of RL policies
- Implement and train agents using Deep Q-learning
- Evaluate and improve model performance
- Apply RL to solve complex decision-making problems
Check out the ReinforcementLearning-Policy repository <a href="https://github.com/VITB-Tigers/ReinforcementLearning-Policy">here</a> and start building your own RL agents!