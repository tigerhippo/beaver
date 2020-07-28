from gym_zgame.envs.model.NPC import NPC
#HOW TO DECIDE WHEN TO CHANGE FEAR/TRUST/MORALE AND HOW MUCH TO CHANGE IT
class Lunatic(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 20
        self.morale = 80
        self.trust = 40
        self.personality = "lunatic"
        #self.percent = 0.01 #6th largest percent of population

    def increment_fear(self, increment):
        self.fear = 20
    def increment_morale(self, increment):
        if increment > 0:
            self.morale += increment
    def increment_trust(self, increment):
        self.trust = 40
