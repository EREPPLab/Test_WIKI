from Termination.Termination import Termination


# Terminate when a fitness reaches X or below
class ReversedFitnessTermination(Termination):
    def __init__(self, fitness_goal):
        self.fitness_goal = fitness_goal

    def is_over(self, ga):
        best_fitness = ga.get_best()[1]
        return best_fitness <= self.fitness_goal
