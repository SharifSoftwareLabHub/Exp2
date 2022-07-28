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

    @staticmethod
    def __choose_best_mutation(genome, initial_strings, strings_length, number_of_dashes, mutation_row,
                               longest_string_index, matching_cost, alphabet):
        # mutate 10 step and choose best
        mutated_min_cost = 1000000000
        mutated_string = None
        for i in range(10):
            dashes_indexes = sorted(random.sample(range(strings_length), number_of_dashes))
            temp = Genome.put_dashes_and_get_final_string(dashes_indexes, initial_strings[mutation_row], strings_length)
            cost = Genome.__calc_cost_of_two_strings(genome.genome[longest_string_index], temp, matching_cost, alphabet)
            if cost < mutated_min_cost:
                mutated_string = temp
                mutated_min_cost = cost
        return mutated_string

    @staticmethod
    def mutation(genome, initial_strings, number_of_strings, strings_length, longest_string_index,
                 matching_cost, alphabet):
        new_genome = []
        mutation_row = random.randint(0, number_of_strings - 1)
        number_of_dashes = strings_length - len(initial_strings[mutation_row])
        mutated_string = Genome.__choose_best_mutation(genome, initial_strings, strings_length, number_of_dashes,
                                                       mutation_row, longest_string_index, matching_cost, alphabet)
        for i in range(number_of_strings):
            if i == mutation_row:
                new_genome.append(mutated_string)
            else:
                new_genome.append(copy.copy(genome.genome[i]))
        g = Genome()
        g.genome = new_genome
        return g

    def calc_fitness(self, matching_cost, alphabet, conversion_cost):
        self.fitness = conversion_cost
        for i in range(len(self.genome[0])):
            for j in range(len(self.genome)):
                for z in range(j + 1, len(self.genome)):
                    self.fitness += matching_cost[alphabet[self.genome[j][i]]][alphabet[self.genome[z][i]]]

    def __lt__(self, other):
        return self.fitness < other.fitness
