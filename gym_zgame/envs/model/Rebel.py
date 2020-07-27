from gym_zgame.envs.model.NPC import NPC

class Rebel(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 50
        self.morale = 50
        self.trust = 40
        self.personality = "rebel"
        # self.percent = 0.1 3rd largest percent of population
    
    def increment_trust(self, increment):
        if increment < 0:
            self.trust += increment * 1.5
        else:
            super.increment_trust(increment)
