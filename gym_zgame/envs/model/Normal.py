from gym_zgame.envs.model.Personality import Personality
#REMEMBER TO DOCUMENT CLASSES!
class Normal(Personality): #For people with normal personality
    type_name = "Normal" #Name of person type
    pop_percent = 0.5 #0.5 * total number of people = total number of Normal people

    def __init__(self, fear, trust, morale):
        super().__init__(fear, trust, morale)

    def __format__(self, format):
        super().__format__(format)

    
    