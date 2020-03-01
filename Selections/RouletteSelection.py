import random

from Selections.Selection import Selection


class RouletteSelection(Selection):
    def select(self, ga, population):

        fitnessSum = 0
        for i in range(len(population)):
            fitnessSum += ga.get_fitness(population[i])

        probabilities = []
        for j in range(len(population)):
            probability = ga.get_fitness(population[j]) / fitnessSum
            probabilities.append(probability)

        randomNumber = random.uniform(0, 1)

        partialSum = 0
        parent_index = None
        for k in range(len(probabilities)):
            if parent_index is None:
                if randomNumber <= probabilities[k] + partialSum:
                    parent_index = k
            partialSum = partialSum + probabilities[k]

        return ga.population[parent_index]
