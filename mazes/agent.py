class ZAgent:
    def __init__(self):
        pass

    def take_action(self, environment):
        pass

    def get_reward(self, environment, action):
        pass

    def learn(self, environment, action, reward):
        pass


class Agent:
    def __init__(self):
        self.state_history = None

    def choose_action(self):
        pass

    def update_state_history(self):
        pass

    def learn(self):
        pass