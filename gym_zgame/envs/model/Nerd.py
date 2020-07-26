from gym_zgame.envs.model.NPC import NPC
#SOMETHING THAT AN OBJECT DOES CAN CHANGE THEIR OWN FEAR/TRUST/MORALE
class Nerd(NPC): 
    def __init__(self):
        super().__init__()
        self.fear = 40
        self.morale = 50
        self.trust = 60
        self.personality = "nerd"
        self.mutation = Mutation() #creates new mutation object
        #SHOULD WE MAKE IT SO THAT A MUTATION OBJECT IS CREATED IN A CLASS FOR ALL NERDS
        #SO THAT ONE MUTATION OCCURS INSTEAD OF HAVING THE CHANCE OF GETTING FIVE MUTATIONS FOR FIVE NERDS
        #self.percent = 0.05 #5th largest percent of population
    
    def _getMutation_(self):
        return self.mutation

    def _setMutation_(self, mutation):
        self.mutation = mutation

    def __str__(self):
        percentage = Nerd.pop_percent * 100
        return "This person is of personality type " + Nerd.type_name + ", has a fear level of " + str(self.fear) + ", " + "a trust level of " + str(self.trust) + ", " + "and a morale level of " + str(self.morale) + ", and accounts for " + str(percentage) + "% of the population."

    #may research to try and find a cure
    def _research_(self):
        mutation_occurred = self.mutation.mutation_change() #checks if a mutation occurred
        cure = self.mutation.getCure() #variable stores new chance of finding a cure
        #spread = mutation.getSpread() #variable stores new chance of disease spreading
        #IF WE CONSIDER THE DISEASE SPREAD RATE SHOULD WE RETURN A VARIABLE FOR IT?

        cure_found = False
        if mutation_occurred == True:
            #(cure * 100)% of the time successful cure found
            num = random.randint(0, 100)
            upper_bound = cure * 100

            #if cure is found:
            if num < upper_bound:
                addFear_by = -5
                addTrust_by = 5
                addMorale_by = 5
                factors = [addFear_by, addTrust_by, addMorale_by]
                self.atts.change_allfactors(factors)
                
                cure_found = True
            #if cure is not found:
            else:
                addFear_by = 5
                addTrust_by = 0
                addMorale_by = -5
                factors = [addFear_by, addTrust_by, addMorale_by]
                self.atts.change_allfactors(factors)

        else:
            #10% of the time successful cure found
            num = random.randint(0, 100)

            #if cure is found:
            if num < 10:
                addFear_by = -5
                addTrust_by = 5
                addMorale_by = 5
                factors = [addFear_by, addTrust_by, addMorale_by] 
                self.atts.change_allfactors(factors)

                cure_found = True 
            #if cure is not found:
            else:
                addFear_by = 5
                addTrust_by = 0
                addMorale_by = -5
                factors = [addFear_by, addTrust_by, addMorale_by] 
                self.atts.change_allfactors(factors)

        #necessary to tell another class that the cure impacts the spread of the disease
        return cure_found

    
    #may put themselves in danger to do more research
    def _takeRisk_(self):
        #50% chance of getting disease
        num = random.randint(0, 9)

        risk_taken = False
        if num < 5:
            addFear_by = 1
            addTrust_by = 0
            addMorale_by = -1
            factors = [addFear_by, addTrust_by, addMorale_by] 
            self.atts.change_allfactors(factors)
            risk_taken = True 
            #necessary to tell another class that the risk causes nerds in this neighborhood
            #to get the disease and they should be labeled as sickly/zombie-bitten

        return risk_taken
        
