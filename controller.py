class Controller:
    MAX_GENOMES_STRINGS_LENGTH_INCREMENT_FOR_GA = 5
    instance = None

    def __init__(self):
        self.alphabet_size = 0
        self.alphabet = []
        self.number_of_strings = None
        self.initial_strings = []
        self.conversion_cost = None
        self.matching_cost = []
        self.max_strings_length_index = None
        self.max_strings_length = None
