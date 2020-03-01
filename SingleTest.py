
from GA import GA

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

ga = GA(40, 40, True)  # create a genetic algorithm with 15 chromosomes, each with length 10

# Set the GA values
ga.initialization_impl = RandomInitialization()
ga.mutation_impl = PerGeneMutation(0.03)
ga.selection_impl = TournamentSelection()
ga.crossover_impl = FastSinglePointCrossover()
ga.termination_impl = GenerationTermination(1)
ga.evaluation_impl = SumOfDiffEvaluation2(60)
# ga.evaluation_impl = TestEvaluation()
ga.initialize()

database_csv = ["Index, Selection, Crossover, Mutation, Evaluation,"
                " Termination, Elitism, Generation, Fitness, Chromosome"]
database_index = 0

# Run the GA
start = time.time()

chromosome = [1280] * 40

ga.get_fitness(chromosome)
