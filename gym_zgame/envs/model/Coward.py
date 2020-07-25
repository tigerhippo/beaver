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
    #def _wasteResources_(self):
        #OTHERS' fear increases
        #trust stays the same?
        #morale decreases
        #one deployment already placed in the game gets removed 