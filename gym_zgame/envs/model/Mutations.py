class Mutations:


    def __init__(self, cure, mutation, spread):

        #chance of a cure being found is 1/10
        self.cure = 0.1
        # random number between 0 and 9 (inclusive)
        self.mutation = random.randint(0,9)
        #chance of the disease spreading (positivity rate) is 1/10
        self.spread = 0.1

#getter and setter functions
    def _getCure_(self):
        return self.cure

    def _getMutation_(self):
        return self.mutation

    def _getSpread_(self):
        return self.spread

    def _setCure_(self, cure):
        self.cure = cure

    def _setMutation_(self, mutation):
        self.mutation = mutation

    def _setSpread_(self, spread):
        self.spread = spread

    def mutation_change(self):

        if self.mutation == 0:
            #if mutation occurs, chance of a cure decreases by a factor of 1/2
            self.cure = self.cure/2

            #if mutation occurs, disease spread rate increases by a factor of 2
            self.spread = self.spread*2

