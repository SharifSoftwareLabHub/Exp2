import random
import copy


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

    def random_initialize_genome(self, initial_strings, number_of_strings, strings_length):
        self.genome = []
        for i in range(number_of_strings):
            number_of_dashes = strings_length - len(initial_strings[i])
            if number_of_dashes == 0:
                self.genome.append(initial_strings[i])
                continue
            dashes_indexes = sorted(random.sample(range(strings_length), number_of_dashes))
            self.genome.append(
                Genome.put_dashes_and_get_final_string(dashes_indexes, initial_strings[i], strings_length))

    @staticmethod
    def cross_over(genome1, genome2, number_of_strings):
        children_genome = Genome()
        genome = []
        for i in range(number_of_strings):
            if random.getrandbits(1) == 1:
                genome.append(copy.copy(genome1.genome[i]))
            else:
                genome.append(copy.copy(genome2.genome[i]))
        children_genome.genome = genome
        return children_genome

    @staticmethod
    def __calc_cost_of_two_strings(string1, string2, matching_cost, alphabet):
        cost = 0
        for i in range(len(string1)):
            cost += matching_cost[alphabet[string1[i]]][alphabet[string2[i]]]
        return cost
