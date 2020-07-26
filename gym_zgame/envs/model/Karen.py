from gym_zgame.envs.model.NPC import NPC
#subclass - for people with Karen personality
class Karen(NPC):
    def __init__(self):
        super().__init__()
        self.personality = "karen"
        # self.percent = 0.25

    def __str__(self):
        percentage = Karen.pop_percent * 100
        return "This person is of personality type " + Karen.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    
    #may choose not to follow orders/rules/warnings they believe are useless/stupid
    def _disobey_(self):
        #50% chance they disobey
        num = random.randint(0, 9)

        if num < 5:
            addFear_by = 1 #increases fear by 1 for this neighborhood
            addMorale_by = -1 #decreases fear by 1 for this neighborhood
            addTrust_by = 0 #neither increases nor decreases fear for this neighborhood - fear stays the same
            factors = [addFear_by, addTrust_by, addMorale_by] #list stores all variables for conveniency - these variables will be used very often
            self.atts.change_allfactors(factors) #We are still working on this method call 
            #because it changes fear/morale/trust only for this NPC object. So, we want to give all NPCs
            #an instance variable for which neighborhood they are in, which we can use to change fear/morale/trust
            #for all NPC objects in this neighborhood.


