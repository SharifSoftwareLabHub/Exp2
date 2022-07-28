import random


class Genome:
    def __init__(self):
        self.genome = None
        self.fitness = None

    @staticmethod
    def put_dashes_and_get_final_string(dashes_indexes, string, strings_length):
        chars = []
        string_counter = 0
        dashes_indexes_counter = 0
        for i in range(strings_length):
            if dashes_indexes_counter < len(dashes_indexes) and i == dashes_indexes[dashes_indexes_counter]:
                chars.append('-')
                dashes_indexes_counter += 1
            else:
                chars.append(string[string_counter])
                string_counter += 1
        return ''.join(chars)
