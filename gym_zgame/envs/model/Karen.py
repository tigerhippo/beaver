from gym_zgame.envs.model.NPC import NPC

#subclass - for people with Karen personality
class Karen(NPC):
    def __init__(self):
        super().__init__()
        self.personality = "karen"
        # self.percent = 0.25