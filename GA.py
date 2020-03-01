class GA:
    def __init__(self, population_size, chromosome_length, elitism):
        self.initialization_impl = None
        self.selection_impl = None
        self.mutation_impl = None
        self.crossover_impl = None
        self.evaluation_impl = None  # fitness function
        self.termination_impl = None  # when to stop
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.generation = 0
        self.population = []
        self.fitness_cache = {}
        self.elitism = elitism

    def initialize(self):
        # Create the first population
        self.population = self.initialization_impl.initialize(self.population_size, self.chromosome_length)

    def is_over(self):
        return self.termination_impl.is_over(self)

    def get_fitness(self, chromosome):
        key = ''.join(str(e) for e in chromosome)
        # print(key)
        if key in self.fitness_cache:
            # print("\tFound value in cache to be: " + str(self.fitness_cache[key]))
            return self.fitness_cache[key]
        else:
            fitness = self.evaluation_impl.get_fitness(chromosome)
            self.fitness_cache[key] = fitness
            # print("\tCalculated the fitness to be: " + str(fitness))
            return fitness

    def evolve(self):
        next_population = []
        
        i = 0
        
        # Elitism
        if self.elitism:
            next_population.append(self.get_best()[0])
            i = 1

        while i < self.population_size:
            parent1 = self.selection_impl.select(self, self.population)
            parent2 = self.selection_impl.select(self, self.population)
            offspring = self.crossover_impl.crossover(self, parent1, parent2)
            mutated_offspring = self.mutation_impl.mutate(offspring)
            next_population.append(mutated_offspring)
            i += 1
        self.population = next_population
        self.generation += 1

    def get_best(self):
        best_chromosome = None
        best_fitness = -1
        for i in range(self.population_size):
            chromosome = self.population[i]
            fitness = self.get_fitness(chromosome)
            if fitness <= best_fitness or best_chromosome is None:
                best_fitness = fitness
                best_chromosome = chromosome
        return [best_chromosome, best_fitness]
