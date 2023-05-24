import random

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Agent's initial position

    def perceive(self):
        x, y = self.position
        return self.environment[x][y]  # Perception is the current state of the environment

    def decide(self, perception):
        if perception == 'A':
            return 'Move Up'
        elif perception == 'B':
            return 'Move Right'
        else:
            return 'Random Move'

    def act(self, action):
        if action == 'Move Up':
            self.position = (self.position[0] - 1, self.position[1])
        elif action == 'Move Right':
            self.position = (self.position[0], self.position[1] + 1)
        elif action == 'Random Move':
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            self.position = (self.position[0] + dx, self.position[1] + dy)

# Define the environment
environment = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

# Create an instance of the agent
agent = Agent(environment)

# Agent perceives the environment
perception = agent.perceive()

# Agent makes a decision based on the perception
action = agent.decide(perception)

# Agent takes action
agent.act(action)

# Agent's new position
print("Agent's new position:", agent.position)
