#REMEMBER TO DOCUMENT CLASSES!
#Personality class is the superclass for all other classes pertaining to personalities
class Personality:
    type_name = " " #class variable - does not change - name for this personality type
    pop_percent = 0.0 #class variable - does not change - percentage of population which has this type of personality

    #put pop_percent variable into init as instance variable
    def __init__(self, fear, trust, morale): #instance variables are initiated - these may change and thus have getters and setters
        self.fear = fear #int value
        self.trust = trust #int value
        self.morale = morale #int value
    
    #getters and setters are not written in subclasses but can still be called by subclasses
    
    def _getFear_(self):
        return self.fear
    
    def _getTrust_(self):
        return self.trust

    def _getMorale_(self):
        return self.morale

    def _setFear_(self, fear):
        self.fear = fear

    def _setTrust_(self, trust):
        self.trust = trust

    def _setMorale_(self, morale):
        self.morale = morale

    def __str__(self): #displays a clear representation of all important attributes this object has
        percentage = Personality.pop_percent * 100
        return "This person is of personality type " + Personality.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."
    
