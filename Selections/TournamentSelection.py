import random

from Selections.Selection import Selection


class TournamentSelection(Selection):
    def select(self, ga, population):
        parent1 = population[random.randint(0, len(population) - 1)]
        parent2 = population[random.randint(0, len(population) - 1)]
        fitness1 = ga.get_fitness(parent1)
        fitness2 = ga.get_fitness(parent2)

        if fitness1 <= fitness2:
            return parent1
        else:
            return parent2
