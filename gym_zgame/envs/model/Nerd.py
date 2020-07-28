from gym_zgame.envs.model.NPC import NPC
#SOMETHING THAT AN OBJECT DOES CAN CHANGE THEIR OWN FEAR/TRUST/MORALE
class Nerd(NPC): 
    def __init__(self):
        super().__init__()
        self.fear = 40
        self.morale = 50
        self.trust = 60
        self.personality = "nerd"
        #self.percent = 0.05 #5th largest percent of population
    
    def increment_fear(self, increment):
        if increment > 0:
            self.fear += increment * 0.5
        else:
            super.increment_fear(increment)
    def increment_morale(self, increment):
        if increment > 0:
            self.morale += increment * 1.5
        else:
            super.increment_fear(increment)
