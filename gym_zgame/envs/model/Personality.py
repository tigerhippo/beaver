#REMEMBER TO DOCUMENT CLASSES!
class Personality:
    #fear = 0
    #trust = 0
    #morale = 0
    type_name = " "
    pop_percent = 0.0

    #def __init__(self, fear, trust, morale, type_name, pop_percent):
        #self.fear = fear
        #self.trust = trust
        #self.morale = morale
        #self.type_name = type_name
        #self.pop_percent = pop_percent

    def __init__(self, fear, trust, morale):
        self.fear = fear
        self.trust = trust
        self.morale = morale
    
    def _getFear_(self):
        return self.fear
    
    def _getTrust_(self):
        return self.trust

    def _getMorale_(self):
        return self.morale
    
    #def _getTypeName_(self):
        #return self.type_name
    
    #def _getPopPercent_(self):
        #return self.pop_percent

    def _setFear_(self, fear):
        self.fear = fear

    def _setTrust_(self, trust):
        self.trust = trust

    def _setMorale_(self, morale):
        self.morale = morale

    #def _setTypeName_(self, type_name):
        #self.type_name = type_name

    #def _setPopPercent_(self, pop_percent):
        #self.pop_percent = pop_percent

    #def __format__(self, format):
        #percentage = self.pop_percent * 100
        #return "This person is of personality type " + self.type_name + " has a fear level of " + self.fear + ", " + "a trust level of " + self.trust + ", " + "and a morale level of " + self.morale + " and accounts for " + percentage + "% of the population."

    def __format__(self, format):
        percentage = Personality.pop_percent * 100
        return "This person is of personality type " + Personality.type_name + " has a fear level of " + self.fear + ", " + "a trust level of " + self.trust + ", " + "and a morale level of " + self.morale + " and accounts for " + percentage + "% of the population."
    
