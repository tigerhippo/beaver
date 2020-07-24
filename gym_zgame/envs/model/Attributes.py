
class Attributes:
    def __init__(self, fear, morale, trust):
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

    def increment_fear(self, num):
        self.fear += num
    def increment_morale(self, num):
        self.morale += num    
    def increment_trust(self, num):
        self.trust += num