from  GeneticAlgorithm import GeneticAlgorithm
import sys

class Controller:
    MAX_GENOMES_STRINGS_LENGTH_INCREMENT_FOR_GA = 5
    instance = None

    def __init__(self):
        self.alphabet_size = None
        self.alphabet = []
        self.number_of_strings = None
        self.initial_strings = []
        self.conversion_cost = None
        self.matching_cost = []
        self.max_strings_length_index = None
        self.max_strings_length = None

    def start(self):
            self.__get_inputs()
            self.__calc_max_string_length_index()
            for strings_length in range(self.max_strings_length,
                                        self.max_strings_length + Controller.MAX_GENOMES_STRINGS_LENGTH_INCREMENT_FOR_GA):
                ga = GeneticAlgorithm(self.initial_strings, strings_length, self.matching_cost,
                        self.alphabet, self.__calc_initial_conversion_cost(strings_length), self.max_strings_length_index)
                ga.start(60)    # algorithm run's time for specific strings_length
                print("\nSTRINGS LENGTH FOR GA INCREMENTED\n", file=sys.stderr)
            GeneticAlgorithm.print_best_genome(sys.stdout)
    
    def __get_inputs(self):
        pass

    def __calc_max_string_length_index(self):
        pass

    def __calc_initial_conversion_cost(self, strings_length):
        pass