from gym_zgame.envs.model.NPC import NPC
#KEEP IN MIND THAT EVERYONE IS REPRESENTED BY ONE INSTANCE - INDIVIDUALS SHOULD BE CONSIDERED AS WELL
#SOMETHING THAT AN OBJECT DOES CAN CHANGE THEIR OWN FEAR/TRUST/MORALE
class Nerd(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 40
        self.morale = 50
        self.trust = 60
        self.personality = "nerd"
        # self.percent = 0.05 5th largest percent of population

    #may research to try and find a cure
    def _research_(self):
        #10% of the time successful cure found
        num = random.randint(0, 9)
        
        #cure_found = False
        if num == 0:
            addFear_by = -5
            addTrust_by = 5
            addMorale_by = 5
            factors = [addFear_by, addTrust_by, addMorale_by] 
            self.atts.change_allfactors(factors)
            #cure_found = True 
            #necessary to tell another class that the cure impacts the spread of the disease
        
        #return cure_found
    
    #may put themselves in danger to do more research
    def _takeRisk_(self):
        #50% chance of getting disease
        num = random.randint(0, 9)

        #risk_taken = False
        if num < 5:
            addFear_by = 1
            addTrust_by = 0
            addMorale_by = -1
            factors = [addFear_by, addTrust_by, addMorale_by] 
            self.atts.change_allfactors(factors)
            #risk_taken = True 
            #necessary to tell another class that the risk causes nerds in this neighborhood
            #to get the disease and they should be labeled as sickly/zombie-bitten

        #return risk_taken
        
