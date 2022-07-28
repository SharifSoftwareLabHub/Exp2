import time
import sys
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

    def start(self, search_time):
        descendants = 0
        start_time = time.time()
        while time.time() - start_time < search_time:
            descendants += 1
            self.__selection()
            self.__cross_over()
            self.__mutation()
        print("Number of descendants:", descendants, file=sys.stderr)
    
    def __selection(self):
        pass

    def __cross_over(self):
        pass

    def __mutation(self):
        pass