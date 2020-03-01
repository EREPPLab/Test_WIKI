from Termination.Termination import Termination


class GenerationTermination(Termination):
    def __init__(self, max_generation):
        self.max_generation = max_generation

    def is_over(self, ga):
        return ga.generation >= self.max_generation
