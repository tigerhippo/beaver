
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

    def increment_fear(self, num):
        self.fear += num
    def increment_morale(self, num):
        self.morale += num    
    def increment_trust(self, num):
        self.trust += num