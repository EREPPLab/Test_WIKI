import random

from Crossover.Crossover import Crossover


class MultiPointCrossover(Crossover):
    def crossover(self, ga, parent1, parent2):
        chromosome_length = len(parent1)

        parents = [parent1, parent2]

        n = 2
        offspring_1 = []
        offspring_2 = []

        count = tmpCount = 0
        pSwitch = 0

        for i in range(n):
            count = random.randint(count, chromosome_length)
            offspring_1.extend(parents[pSwitch][tmpCount:count])
            if (pSwitch == 1):
                pSwitch = 0
            else:
                pSwitch = 1
            offspring_2.extend(parents[pSwitch][tmpCount:count])
            tmpCount = count

        offspring_1.extend(parents[pSwitch][tmpCount:])
        if (pSwitch == 1):
            pSwitch = 0
        else:
            pSwitch = 1
        offspring_2.extend(parents[pSwitch][tmpCount:])

        fitness_1 = ga.get_fitness(offspring_1)
        fitness_2 = ga.get_fitness(offspring_2)

        if fitness_1 >= fitness_2:
            return offspring_1
        else:
            return offspring_2