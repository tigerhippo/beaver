from gym_zgame.envs.model.NPC import NPC

class Coward(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 60
        self.morale = 50
        self.trust = 50
        self.personality = "coward"
        # self.percent = 0.09 4th largest percent of population
    
    def increment_fear(self, increment):
        if increment > 0:
            self.fear += (increment * 1.5)
        else:
            super.increment_fear(increment)
    def increment_morale(self, increment):
        if increment > 0:
            self.morale += (increment * 0.75)
        else:
            super.increment_morale(increment)