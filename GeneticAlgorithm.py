from genome import Genome

class GeneticAlgorithm:
    def __init__(self, initial_strings, strings_length):
        self.initial_strings = initial_strings
        self.strings_length = strings_length
        self.number_of_strings = len(initial_strings)
        self.population = self.__make_initial_population()
        
    def __make_initial_population(self):
        population = [Genome() for i in range(GeneticAlgorithm.POPULATION_SIZE)]
        for genome in population:
            genome.random_initialize_genome(self.initial_strings, self.number_of_strings, self.strings_length)
        return population
