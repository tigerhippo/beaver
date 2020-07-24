from gym_zgame.envs.model.NPC import NPC
from gym_zgame.envs.model.Attributes import Attributes
#SHOULD TRUST DECREASE HERE NECESSARILY
#HOW TO DECIDE WHEN TO CHANGE FEAR/TRUST/MORALE AND HOW MUCH TO CHANGE IT
#HOW TO DECIDE WHAT THE STARTING LEVELS ARE AND HOW THE OBJECT THEMSELVES ARE IMPACTED
class Lunatic(NPC):
    def __init__(self):
        super().__init__()
        self.atts = Attributes(0, 20, 80, 40)
        self.personality = "lunatic"
        self.percent = 0.01 #6th largest percent of population

    def __str__(self):
        percentage = Lunatic.pop_percent * 100
        return "This person is of personality type " + Lunatic.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."

    #may choose not to follow orders/rules/warnings
    def _disobey_(self):
        addFear_by = 3 #increases OTHERS' fear by 3
        addTrust_by = 0 #fear stays the same
        addMorale_by = -3 #decreases fear by 3
        factors = [addFear_by, addTrust_by, addMorale_by] #stores variables for conveniency and future usage
        return factors
    
    #may choose to infect others on purpose due to craziness
    #def _infectOthers_(self):
        #50% chance they can infect others
        #if they do a random 1% of the population gets infected

        #OTHERS' fear increases
        #trust stays the same?
        #morale decreases
        #lunatic morale increases?