from gym_zgame.envs.model.NPC import NPC
#subclass - for people with Karen personality
class Karen(NPC):
    def __init__(self):
        super().__init__()
        self.atts = Attributes(0, 50, 50, 50)
        self.personality = "karen"
        self.percent = 0.25

    def __str__(self):
        percentage = Karen.pop_percent * 100
        return "This person is of personality type " + Karen.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    
    #may choose not to follow orders/rules/warnings they believe are useless/stupid
    def _disobey_(self):
        addFear_by = 1 #increases OTHERS' fear by 1
        addTrust_by = 0 #neither increases nor decreases fear - fear stays the same
        addMorale_by = -1 #decreases fear by 1
        factors = [addFear_by, addTrust_by, addMorale_by] #list stores all variables for conveniency - these variables will be used very often
        return factors
