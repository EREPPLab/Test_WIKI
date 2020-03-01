import random

from Constants import Constants
from Initialization.Initialization import Initialization


class RandomInitialization(Initialization):
    def initialize(self, population_size, chromosome_length):
        population = []
        for i in range(population_size):
            chromosome = []
            for j in range(chromosome_length):
                random_gene = random.randint(Constants.gene_lower_bound, Constants.gene_upper_bound)
                chromosome.append(random_gene)
            population.append(chromosome)
        return population
