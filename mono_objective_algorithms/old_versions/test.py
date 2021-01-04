import time
import csv

from data_structure.Problem import Problem
from mono_objective_algorithms.algorithms.main.hybrid import ABCgenetic
from mono_objective_algorithms.algorithms.operations.fitness import fit



# main

# input
n_act = int(input("NUMBER OF ACTIVITIES : "))
n_candidates = int(input("NUMBER OF CANDIDATE SERVICES : "))
constraints = {'responseTime': n_act * 5 , 'price': n_act * 3, 'availability': 0.9 ** n_act, 'reliability': 0.7 ** n_act}
weights = [0.25, 0.25, 0.25, 0.25]
mcn = int(input("ITERATION NUMBER : "))
sq = int(input("SCOUTS CONDITION : "))


# problem init

p = Problem(n_act , n_candidates , constraints , weights)


# optimal fitness
print("optimal fitness search !")
opt , _ , _ , _ , _=  ABCgenetic(problem = p ,SQ = 100, SN = 100 , MCN=mcn * 10, SCP=(4*mcn) //5 , N=100, CP=0.8)
print("\nDone !")

# executing scenario

print("Executing Algorithm ")
start_time = time.time()
result , minQos , maxQos , _ , _= ABCgenetic(problem = p ,SQ = sq, SN = 100 , MCN=mcn , SCP=(4*mcn) //5 , N=100, CP=0.8)
rt = time.time() - start_time

normalized_fitness = fit(result, minQos , maxQos , weights) / fit(opt, minQos , maxQos , weights)

with open('test_results.csv', mode='a') as file:
    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow([n_act,n_candidates,100,sq, mcn, normalized_fitness ,rt])

print(f"Scalability = {rt} Fitness = {normalized_fitness}")
