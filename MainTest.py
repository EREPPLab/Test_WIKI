from GA import GA
from Database import Database

from Initialization.RandomInitialization import RandomInitialization

from Selections.RouletteSelection import RouletteSelection
from Selections.TournamentSelection import TournamentSelection

from Crossover.SinglePointCrossover import SinglePointCrossover
from Crossover.FastSinglePointCrossover import FastSinglePointCrossover
from Crossover.MultiPointCrossover import MultiPointCrossover

from Mutations.PerGeneMutation import PerGeneMutation

from Termination.FitnessTermination import FitnessTermination
from Termination.GenerationTermination import GenerationTermination
from Termination.ReversedFitnessTermination import ReversedFitnessTermination

from Evaluation.TestEvaluation import TestEvaluation
from Evaluation.RealEvaluation import RealEvaluation
from Evaluation.SumOfDiffEvaluation import SumOfDiffEvaluation
from Evaluation.SumOfDiffEvaluation2 import SumOfDiffEvaluation2

import time

# Create the Database object to send and receive data
Database = Database()

# A TRIAL is one full iteration of the GA algorithm
Number_of_trials = 5

# Send the robot name to the database
Robot_UID = Database.Get_Robot_UID("Simulation")

# Population Size / Chromosome Length
Population_size = 100
Chromosome_length = 10
# Total number of Generations
Total_generations = 60

# Mutation rate (Small numbers)
Mutation_rate = 0.03


# ------------ Do not manipulate variables ----------- #

# Trial starting point
Current_trial = 0

while Current_trial < Number_of_trials:
    print("Trial Count: " + str(Current_trial))

    # Start time to see how long it takes in seconds to run
    start = time.time()

    # Start of GA configuration
    ga = GA(Population_size, Chromosome_length, True)

    # Set the GA Configuration
    ga.initialization_impl = RandomInitialization()
    ga.mutation_impl = PerGeneMutation(Mutation_rate)
    ga.selection_impl = TournamentSelection()
    ga.crossover_impl = FastSinglePointCrossover()
    ga.termination_impl = GenerationTermination(Total_generations)
    # ga.evaluation_impl = SumOfDiffEvaluation2(60) <-- Used for testing robot
    ga.evaluation_impl = TestEvaluation()
    ga.initialize()

    # Config UID is check in the database and added if necessary
    if Current_trial == 0:
        Config_UID = Database.Get_Config_UID(type(ga.selection_impl).__name__,
                                             type(ga.crossover_impl).__name__,
                                             type(ga.mutation_impl).__name__,
                                             type(ga.evaluation_impl).__name__,
                                             type(ga.termination_impl).__name__,
                                             True,
                                             Population_size,
                                             Chromosome_length,
                                             Mutation_rate)

    # Temporary variable to store each generation to add to Database
    Generation = []
    # Run the GA
    while not ga.is_over():
        ga.evolve()
        best = ga.get_best()
        print("Curent Trial " + str(Current_trial))
        print("Generation #" + str(ga.generation))
        print("\tBest Fitness = " + str(best[1]))

        # ---------- Each Chromosome ---------- #
        for i in range(len(ga.population)):
            chromosome = ga.population[i]
            # Get the fitness of the current chromosome
            fitness = ga.get_fitness(chromosome)
            # Add to Database list
            chromosome_string = ' '.join(map(str, chromosome))
            # Database.Add_run(Config_UID, ga.generation, fitness, Current_trial, str(chromosome_string), Robot_UID)
            Generation.append([ga.generation, fitness, Current_trial, str(chromosome_string), Robot_UID])
            # Print Chromosome - Fitness
            # print("\t" + str(ga.population[i]) + " - " + str(ga.get_fitness(ga.population[i])))
            print("\t Chromosome #" + str(i) + " - " + str(ga.get_fitness(ga.population[i])))
        # ---------- Each Generation ---------- #
        # Print the Cache and how many elements
        print("\tCache has " + str(len(ga.fitness_cache.keys())) + " elements.")
        # Add each generation to the database
        Database.Add_generation(Generation, Config_UID)
        # Empty the generation so we don't add it on the next
        Generation = []
    # ---------- Each Trial ---------- #
    Current_trial += 1

end = time.time()
print("Simulation took " + str(end - start) + " seconds.")

# End connection
Database.End_connection()
