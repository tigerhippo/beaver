from gym_zgame.envs.model.NPC import NPC

class Coward(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 60
        self.morale = 50
        self.trust = 50
        self.personality = "coward"
        # self.percent = 0.09 4th largest percent of population

    def __str__(self):
        percentage = Coward.pop_percent * 100
        return "This person is of personality type " + Coward.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    
    #may use up more resources than necessary out of fear
    def _wasteResources_(self):
        #50% chance that the coward chooses to waste resources
        num = random.randint(0, 9)

        #resources_wasted = False
        if num < 5:
            addFear_by = 1
            addTrust_by = 0
            addMorale_by = -1
            factors = [addFear_by, addTrust_by, addMorale_by] 
            self.atts.change_allfactors(factors)
            #resources_wasted = True 
            #necessary to tell another class that a deployment should be removed

        #return resources_wasted