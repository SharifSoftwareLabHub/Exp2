from GeneticAlgorithm import GeneticAlgorithm
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

    @staticmethod
    def get_instance():
        if Controller.instance is None:
            Controller.instance = Controller()
        return Controller.instance

    def start(self):
        self.__get_inputs()
        self.__calc_max_string_length_index()
        for strings_length in range(self.max_strings_length,
                                    self.max_strings_length + Controller.MAX_GENOMES_STRINGS_LENGTH_INCREMENT_FOR_GA):
            ga = GeneticAlgorithm(self.initial_strings, strings_length, self.matching_cost,
                                  self.alphabet, self.__calc_initial_conversion_cost(strings_length),
                                  self.max_strings_length_index)
            ga.start(60)  # algorithm run's time for specific strings_length
            print("\nSTRINGS LENGTH FOR GA INCREMENTED\n", file=sys.stderr)
        GeneticAlgorithm.print_best_genome(sys.stdout)

    def __get_inputs(self):
        self.alphabet_size = int(input())
        self.alphabet = dict()
        alphabet = input().split(', ')
        for i, char in enumerate(alphabet):
            self.alphabet[char] = i
        self.alphabet['-'] = self.alphabet_size
        self.number_of_strings = int(input())
        for i in range(self.number_of_strings):
            self.initial_strings.append(input())
        self.conversion_cost = int(input())
        for i in range(self.alphabet_size + 1):
            self.matching_cost.append(list(map(int, input().split(' '))))

    def __calc_max_string_length_index(self):
        max_strings_length = 0
        max_strings_length_index = None
        for i, string in enumerate(self.initial_strings):
            if max_strings_length < len(string):
                max_strings_length = len(string)
                max_strings_length_index = i
        self.max_strings_length_index = max_strings_length_index
        self.max_strings_length = len(self.initial_strings[self.max_strings_length_index])

    def __calc_initial_conversion_cost(self, strings_length):
        pass


Controller.get_instance().start()
