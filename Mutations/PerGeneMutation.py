import random

from Constants import Constants
from Mutations.Mutation import Mutation


class PerGeneMutation(Mutation):
    def __init__(self, mutation_chance):
        self.mutation_chance = mutation_chance  # 10% = 0.10

    def mutate(self, chromosome):
        mutated = []
        for i in range(len(chromosome)):
            if random.random() < self.mutation_chance:  # mutate
                random_gene = random.randint(Constants.gene_lower_bound, Constants.gene_upper_bound)
                mutated.append(random_gene)
            else:  # didn't mutate this gene
                mutated.append(chromosome[i])
        return mutated

    '''
    def __str__(self):
        return "PerGeneMutation rate=" + str(self.mutation_chance);
    
    '''
