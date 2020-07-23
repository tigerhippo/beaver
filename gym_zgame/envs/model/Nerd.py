from gym_zgame.envs.model.Personality import Personality
#KEEP IN MIND THAT EVERYONE IS REPRESENTED BY ONE INSTANCE - INDIVIDUALS SHOULD BE CONSIDERED AS WELL
#SOMETHING THAT AN OBJECT DOES CAN CHANGE THEIR OWN FEAR/TRUST/MORALE
class Nerd(Personality):
    type_name = "Nerd"
    pop_percent = 0.05 #5th largest percent of population

    def __init__(self, fear, trust, morale):
        super().__init__(fear, trust, morale)

    def __str__(self):
        percentage = Nerd.pop_percent * 100
        return "This person is of personality type " + Nerd.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."

    #may research to try and find a cure
    #def _research_(self):
        #10% of the time successful cure found
        #90% of the time not found

        #if cure is found
        #fear decreases
        #trust increases
        #morale increases
    
    #may put themselves in danger to do more research
    #def _takeRisk_(self):
        #50% chance of getting disease
        #5% of total Nerd population gets disease 

        #if they get the disease
        #label as sickly or zombie-bitten
        #OTHERS' fear increases 
        #trust decreases
        #morale decreases
