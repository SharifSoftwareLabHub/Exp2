import time
import sys
import random
import math
from genome import Genome

class GeneticAlgorithm:
    POPULATION_SIZE = 40
    MAX_VALUE = 1000000000
    REMAIN_DESCENDANT_SIZE_PER_POPULATION = 0.2

    best_genome = Genome()
    best_genome.fitness = MAX_VALUE

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
        self.__calc_genomes_fitness()
        self.population.sort()
        del self.population[int(GeneticAlgorithm.REMAIN_DESCENDANT_SIZE_PER_POPULATION * len(self.population)):]
        if self.population[0].fitness < GeneticAlgorithm.best_genome.fitness:
            GeneticAlgorithm.best_genome = self.population[0]
            GeneticAlgorithm.print_best_genome(sys.stderr)
        probabilities = self.__calc_population_probability()
        self.population = random.choices(self.population, probabilities, k=GeneticAlgorithm.POPULATION_SIZE)

    def __calc_genomes_fitness(self):
        for genome in self.population:
            if genome.fitness is None:
                genome.calc_fitness(self.matching_cost, self.alphabet, self.conversion_cost)

    def __calc_population_probability(self):
        probabilities = []
        for genome in self.population:
            if genome.fitness is None:
                genome.calc_fitness(self.matching_cost, self.alphabet, self.conversion_cost)
            probability = math.pow(genome.fitness, -3)
            probabilities.append(probability)
        return probabilities 
    
    def __cross_over(self):
        pass
    
    def __mutation(self):
        pass

    @staticmethod
    def print_best_genome(stdout_or_err):
        print(GeneticAlgorithm.best_genome.fitness, file=stdout_or_err)
        for string in GeneticAlgorithm.best_genome.genome:
            print(string, file=stdout_or_err)
        print(file=stdout_or_err)