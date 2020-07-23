from Personality import Personality
#subclass - for people with normal personality
class Normal(Personality): 
    type_name = "Normal" 
    pop_percent = 0.5 #largest percent of population

    #no extra methods other than the ones the class implements from Personality 
    def __init__(self, fear, trust, morale):
        super().__init__(fear, trust, morale)

    def __str__(self):
        percentage = Normal.pop_percent * 100
        #make this part more readable
        return "This person is of personality type " + Normal.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    



    