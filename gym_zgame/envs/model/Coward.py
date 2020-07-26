from gym_zgame.envs.model.NPC import NPC

class Coward(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 60
        self.morale = 50
        self.trust = 50
        self.personality = "coward"
        # self.percent = 0.09 4th largest percent of population