from gym_zgame.envs.model.NPC import NPC

class Rebel(NPC):
    def __init__(self):
        super().__init__()
        self.fear = 50
        self.morale = 50
        self.trust = 40
        self.personality = "rebel"
        # self.percent = 0.1 3rd largest percent of population

    def __str__(self):
        percentage = Rebel.pop_percent * 100
        return "This person is of personality type " + Rebel.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    
    #may choose not to follow orders/rules/warnings 
    def _disobey_(self):
        addFear_by = 2 #increases OTHERS' fear by 1
        addTrust_by = 0 #neither increases nor decreases fear - fear stays the same
        addMorale_by = -2 #decreases fear by 1
        factors = [addFear_by, addTrust_by, addMorale_by] #list stores all variables for conveniency - these variables will be used very often
        return factors

    #may choose to start a riot to rebel against authority
    #def _startRiot_(self):
        #OTHERS' fear increases A LOT
        #trust decreases A LOT
        #morale decreases A LOT
        #the neighborhood where the riot occurred becomes unavailable for a certain # of turns (people cannot move in/out and no deployments can be placed there)
