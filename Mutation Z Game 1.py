import random

class Mutation:

    def __init__(self, cure = 0.1, mutation = random.randint(0,9), spread = 0.1):

        #chance of a cure being found is 1/10
        self.cure = cure
        # random number between 0 and 9 (inclusive)
        self.mutation = mutation
        #chance of the disease spreading (positivity rate) is 1/10
      #  self.spread = spread


#getter and setter functions
    def _getCure_(self):
        return self.cure

    def _getMutation_(self):
        return self.mutation

    #def _getSpread_(self):
     #   return self.spread

    def _setCure_(self, cure):
        self.cure = cure

    def _setMutation_(self, mutation):
        self.mutation = mutation

    #def _setSpread_(self, spread):
     #   self.spread = spread

    def mutation_change(self):
        mutationOccurred == False
        mutationNumbers == 0

        if self.mutation == 0:
            #if mutation occurs, chance of a cure decreases by a factor of 1/2
            self.cure = self.cure/2
            mutationNumbers = MutationNumbers + 1
                mutationOccurred = True


            #if mutation occurs, disease spread rate increases by a factor of 2
      #      self.spread = self.spread*2
            return mutationOccured


