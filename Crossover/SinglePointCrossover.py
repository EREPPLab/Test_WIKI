import random

from Crossover.Crossover import Crossover


class SinglePointCrossover(Crossover):
    def crossover(self, ga, parent1, parent2):
        chromosome_length = len(parent1)
        random_index = random.randint(0, chromosome_length)
        offspring_1 = []
        offspring_2 = []

        offspring_1.extend(parent1[0:random_index])
        offspring_1.extend(parent2[random_index:])

        offspring_2.extend(parent1[0:random_index])
        offspring_2.extend(parent2[random_index:])

        fitness_1 = ga.get_fitness(offspring_1)
        fitness_2 = ga.get_fitness(offspring_2)

        if fitness_1 >= fitness_2:
            return offspring_1
        else:
            return offspring_2
