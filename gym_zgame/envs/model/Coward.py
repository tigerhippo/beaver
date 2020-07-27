from gym_zgame.envs.model.Personality import Personality

class Coward(Personality):
    type_name = "Coward"
    pop_percent = 0.09 #4th largest percent of population

    def __init__(self, fear, trust, morale):
        super().__init__(fear, trust, morale)

    def __str__(self):
        percentage = Coward.pop_percent * 100
        return "This person is of personality type " + Coward.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    
    #may use up more resources than necessary out of fear
    #def _wasteResources_(self):
        #OTHERS' fear increases
        #trust stays the same?
        #morale decreases
        #one deployment already placed in the game gets removed 