from gym_zgame.envs.model.Personality import Personality

class Karen(Personality):
    type_name = "Karen"
    pop_percent = 0.25

    def __init__(self, fear, trust, morale):
        super().__init__(fear, trust, morale)

    def __format__(self, format):
        super().__init__(format)
    
    #def __disobey__(self)
        #some int variable for fear that is shared across all Person objects = higher level of fear
        #return variable

        #or

        #some boolean variable for whether fear should be increased or not = true
        #some int variable for how much fear should be increased = certain number for increase in fear
        #return tuple containing boolean + int