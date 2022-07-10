# This is a sample Python script.
import random

from population import Population

import constants as const
import matplotlib.pyplot as plt


def main():
    initial_size = 100
    average_person_death_age = 60
    population_proportion_mutated = 0.1
    number_of_generations = 100

    population = Population(
        initial_size=initial_size,
        average_person_death_age=average_person_death_age)

    population_sizes_at_varying_generations = []
    people_with_bad_traits_ratio = []
    young_people = []
    old_people = []
    for generation in range(0, number_of_generations):
        people_with_bad_trait = len(population.get_all_people_exhibiting_trait(const.CANNOT_REPRODUCE_GENE))
        print(f"People with bad trait: {people_with_bad_trait} with ratio {people_with_bad_trait/(population.size()+1)}")
        people_with_bad_traits_ratio.append(0 if population.size() == 0 else people_with_bad_trait/population.size())

        population.eliminate_persons_with_bad_genes()

        population.reproduce_generation()
        # population.add_some_genetic_mutations(population_proportion=population_proportion_mutated)

        population.age_population()
        population.eliminate_old_persons()
        print(len(population.population))
        young_people.append(len(population.get_all_people_younger_than(20)))
        old_people.append(len(population.get_all_people_older_than(40)))

        population_sizes_at_varying_generations.append(population.size())

    print(f"Population size: {population.size()}")
    print(f"People with blue eyes: {len(population.get_all_people_exhibiting_trait(const.HAS_BLUE_EYES_GENE))}")
    print(f"People with blonde hair: {len(population.get_all_people_exhibiting_trait(const.HAS_BLONDE_HAIR_GENE))}")
    print(f"People who cannot reproduce: {len(population.get_all_people_exhibiting_trait(const.CANNOT_REPRODUCE_GENE))}")

    plt.xlabel('Generation number')
    plt.title(f"Average death age: {average_person_death_age}, population mutation proportion: {population_proportion_mutated}")
    plt.plot(young_people, color='b', label='young-people')
    plt.plot(old_people, color='r', label='old-people')
    plt.plot(population_sizes_at_varying_generations, color='g', label='population-size')
    plt.legend()
    plt.show()
    plt.ylabel('Ratio of bad traits population vs population')
    # plt.plot(people_with_bad_traits_ratio, color='r')
    # plt.show()

    person_has_recessive_gene = True
    person_has_dominant_gene = False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
