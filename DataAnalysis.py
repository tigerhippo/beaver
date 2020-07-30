import matplotlib.pyplot as plt
import random
import json

class DataAnalysis:

    #with open('data.json') as json_file: #file contains json objects but is not of json type
        #data = json_file.readlines() #read in all lines in file 
        #step_deployments_used = [] #stores deployments used for each step across all steps
        #step_score = [] #stores scores for each step across all steps
        #for i in range(len(data)): 
            #step = json.loads(data[i]) #step (each line) is json object

            #actions = step['actions']
            #deployment = actions[1]
            #step_deployments_used.append(deployment)

            #reward = step['reward']
            #step_score.append(reward)
            
            #print(step_deployments_used)
            #print(step_score)
        #print(step_deployments_used)
        #print(step_score)
    
    #GAME NUMBER VS. SCORE FOR HUMAN
    plt.style.use('ggplot')
    
    num_games = [] 
    for i in range(15):
        num_games.append(i)
    
    game_scores_human = [80, 85, 92, 102, 117, 115, 123, 130, 136, 148, 120, 138, 150, 165, 181] #INCREASES STEADILY BUT SLOWLY AT BEGINNING, SOME UPS AND DOWNS, FINALLY LARGER INCREASES TOWARDS END
    
    xpos = [i for i, _ in enumerate(num_games)]

    plt.plot(num_games, game_scores_human)
    plt.xlabel("Game Number")
    plt.ylabel("Score")
    plt.title("Score Changes Over Games/Time for Human Player")
    plt.xticks(xpos, num_games)

    plt.show()

    #GAME NUMBER VS. SCORE FOR MACHINE
    plt.style.use('ggplot')

    game_scores_machine = [150, 154, 158, 163, 172, 182, 190, 200, 208, 218, 230, 245, 261, 268, 287] #STARTS AT MUCH HIGHER SCORE, INCREASES STEADILY BUT SLOWLY AT BEGINNING, LARGER INCREASES TOWARDS MIDDLE AND BEYOND

    plt.plot(num_games, game_scores_machine)
    plt.xlabel("Game Number")
    plt.ylabel("Score")
    plt.title("Score Changes Over Games/Time for Machine Player")
    plt.xticks(xpos, num_games)

    plt.show()

    #DEPLOYMENTS VS. NUMBER OF TIMES USED FOR HUMAN
    plt.style.use('ggplot')

    deployments = []
    for i in range(24):
        deployments.append(i + 1)
    
    num_deployments_used_human = []
    for i in range(24):
        num = random.randint(0, 200) #MAX NUMBER OF DEPLOYMENTS A PERSON COULD REASONABLY USE 
        num_deployments_used_human.append(num)

    xpos_second = [i for i, _ in enumerate(deployments)]
    
    plt.bar(xpos_second, num_deployments_used_human, color='blue')
    plt.xlabel("Deployment Number")
    plt.ylabel("Number of Times Used")
    plt.title("Number of Times Each Deployment was Used for Human Player")
    plt.xticks(xpos_second, deployments)

    plt.show()
    
    #DEPLOYMENTS VS. NUMBER OF TIMES USED FOR MACHINE
    plt.style.use('ggplot')

    num_deployments_used_machine = []
    for i in range(24): 
        num = random.randint(0, 200) #STILL RANDOM BUT MACHINE WOULD USE SOME DIFFERENT DEPLOYMENTS THAN THE PERSON DID MORE OFTEN
        num_deployments_used_machine.append(num)
    
    plt.bar(xpos_second, num_deployments_used_machine, color='blue')
    plt.xlabel("Deployment Number")
    plt.ylabel("Number of Times Used")
    plt.title("Number of Times Each Deployment was Used for Machine Player")
    plt.xticks(xpos_second, deployments)

    plt.show()
    


    

    #USING ACTUAL DATA FROM DATA.JSON FILE:
    #with open('data.json') as json_file: #file contains json objects but is not of json type
        #data = json_file.readlines() #read in all lines in file 
        #step_deployments_used = [] #stores deployments used for each step across all steps
        #step_score = [] #stores scores for each step across all steps
        #for i in range(len(data)): 
            #step = json.loads(data[i]) #step (each line) is json object

            #actions = step['actions']
            #deployment = actions[1]
            #step_deployments_used.append(deployment)

            #reward = step['reward']
            #step_score.append(reward)
            
            #print(step_deployments_used)
            #print(step_score)
        #print(step_deployments_used)
        #print(step_score)
    
    #plt.style.use('ggplot')
    
    #num_steps = []
    #for i in range(len(step_score)):
        #num_steps.append(i)
    
    #xpos = [i for i, _ in enumerate(num_steps)]

    #plt.bar(xpos, step_score, color='blue')
    #plt.xlabel("Turn")
    #plt.ylabel("Score")
    #plt.title("Score vs. Turn Over Time for Human Player")
    #plt.xticks(xpos, num_steps)
    
    #plt.show()

    #TEST:
    #with open('data.json') as json_file:
        #data = json.load(json_file)
        #print(data)

        #plt.style.use('ggplot')

        #keys = data.keys() #strings(text) - x-axis
        #values = data.values() #ints(numbers) - y-axis

        #xpos = [i for i, _ in enumerate(keys)]

        #plt.bar(xpos, values, color='pink')
        #plt.xlabel("Animal Type")
        #plt.ylabel("Rating")
        #plt.title("Ratings for Different Types of Animals")
        #plt.xticks(xpos, keys)

        #plt.show()

    #REFERENCE CODE:
    #class Barchart: 
        #%matplotlib inline
        #plt.style.use('ggplot') 
    
        #x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'] 
        #sizes = [1, 0, 1, 2, 1, 0, 2, 4, 3, 2, 1, 2, 3, 5, 3, 3, 2, 3, 1, 0, 2, 2, 4, 6] 

        #xpos = [i for i, _ in enumerate(x)] 
    
        #plt.bar(xpos, sizes, color='purple') 
        #plt.xlabel("Deployments") 
        #plt.ylabel("Times Used") 
        #plt.title("Deployment Totals") 
        #plt.xticks(xpos, x)

        #plt.show()