class Attributes:
    def __init__(self, group, fear, morale, trust):
        #idk enums so 0 means npc, 1 means neighborhood, 2 means city, change if u want to
        self.group = group
        self.fear = fear
        self.morale = morale
        self.trust = trust

    def get_fear(self):
        return self.fear 
    def get_morale(self):
        return self.fear
    def get_trust(self):
        return self.morale

    def set_fear(self, num):
        self.fear = num
    def set_morale(self, num):
        self.morale = num    
    def set_trust(self, num):
        self.trust = num

    #depending upon whether num is positive/negative/zero, these methods increase, decrease, or make 
    #the fear, morale, and trust levels stay the same
    def change_fear(self, num):
        self.fear += num
    def change_morale(self, num):
        self.morale += num
    def change_trust(self, num):
        self.trust += num

    #takes in a list with numbers for fear, morale, and trust
    #depending upon the numbers, the method changes the fear, morale, and trust levels
    def change_allfactors(self, list):
        self.fear += list[0]
        self.morale += list[1]
        self.trust += list[2]