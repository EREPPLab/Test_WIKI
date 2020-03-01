from Evaluation.Evaluation import Evaluation


class TestEvaluation(Evaluation):
    def get_fitness(self, chromosome):
        fitness = 0
        for i in range(len(chromosome)):
            fitness += abs(1270 - chromosome[i])
            #if chromosome[i] == 1256:
             #   fitness += 1
        return fitness
