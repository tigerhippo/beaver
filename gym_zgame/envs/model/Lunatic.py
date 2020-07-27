from gym_zgame.envs.model.NPC import NPC
#SHOULD TRUST DECREASE HERE NECESSARILY
#HOW TO DECIDE WHEN TO CHANGE FEAR/TRUST/MORALE AND HOW MUCH TO CHANGE IT
#HOW TO DECIDE WHAT THE STARTING LEVELS ARE AND HOW THE OBJECT THEMSELVES ARE IMPACTED
class Lunatic(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 20
        self.morale = 80
        self.trust = 40
        self.personality = "lunatic"
        # self.percent = 0.01 smallest percent of population

    #may choose to infect others on purpose due to craziness
    def _infectOthers_(self):
        #50% chance they can infect others
        num = random.randint(0, 9)

        #others_infected = False
        if num < 5:
            addFear_by = 5
            addTrust_by = -5
            addMorale_by = -5
            factors = [addFear_by, addTrust_by, addMorale_by] 
            self.atts.change_allfactors(factors)
            #others_infected = True
            #necessary to tell another class that 50% of the people in this neighborhood get infected

        #return others_infected

    def increment_fear(self, increment):
        self.fear = 20
    def increment_morale(self, increment):
        if increment > 0:
            self.morale += increment
    def increment_trust(self, increment):
        self.trust = 40