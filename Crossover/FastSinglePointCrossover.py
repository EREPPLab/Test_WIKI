import random

from Crossover.Crossover import Crossover


class FastSinglePointCrossover(Crossover):
    def crossover(self, ga, parent1, parent2):
        chromosome_length = len(parent1)
        random_index = random.randint(0, chromosome_length)
        offspring = []

        offspring.extend(parent1[0:random_index])
        offspring.extend(parent2[random_index:])

        return offspring
