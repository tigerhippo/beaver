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
    
    #may put themselves in danger to do more research
    def _takeRisk_(self):
        #50% chance of getting disease
        num = random.randint(0, 9)

        risk_taken = False
        if num < 5:
            addFear_by = 1
            addTrust_by = 0
            addMorale_by = -1
            factors = [addFear_by, addTrust_by, addMorale_by] 
            self.atts.change_allfactors(factors)
            risk_taken = True 
            #necessary to tell another class that the risk causes nerds in this neighborhood
            #to get the disease and they should be labeled as sickly/zombie-bitten

        #return risk_taken
    
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
