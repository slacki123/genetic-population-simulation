# This is a sample Python script.
import random

import numpy

from population import Population

import constants as const
import matplotlib.pyplot as plt


def main():
    initial_size = 10000
    average_person_death_age = 60
    population_proportion_mutated = 0.1
    number_of_generations = 1000
    average_number_of_children = 2

    population = Population(
        initial_size=initial_size,
        average_person_death_age=average_person_death_age,
        average_number_of_children=average_number_of_children)

    population_sizes_at_varying_generations = []
    people_with_bad_traits_ratio = []
    young_people = []
    old_people = []
    people_who_died_prematurely_ratio = []
    average_death_ages = []
    for generation in range(0, number_of_generations):
        people_with_bad_trait = len(population.get_all_people_exhibiting_trait(const.CANNOT_REPRODUCE_GENE))
        print(f"People with bad trait: {people_with_bad_trait} with ratio {people_with_bad_trait/(population.size()+1)}")
        people_with_bad_traits_ratio.append(0 if population.size() == 0 else people_with_bad_trait/population.size())

        died_prematurely = len(population.get_all_people_exhibiting_trait(const.PREMATURE_DEATH_GENE))
        print(f"People premature death trait: {died_prematurely} with ratio {died_prematurely/(population.size()+1)}")
        people_who_died_prematurely_ratio.append(0 if population.size() == 0 else died_prematurely/(population.size()+1))
        average_death_age = sum([person.death_age for person in population.population])/(population.size() + 1)
        average_death_ages.append(average_death_age)

        population.reproduce_generation()

        population.age_population()
        population.eliminate_old_persons()
        print(len(population.population))
        young_people.append(len(population.get_all_people_younger_than(20)))
        old_people.append(len(population.get_all_people_older_than(40)))

        population_sizes_at_varying_generations.append(population.size())
#        print(f"Average children: {sum([person.number_of_offspring for person in population.get_all_reproductive_females()]) / len(population.get_all_reproductive_females())}")

    print(f"Population size: {population.size()}")
    print(f"People who can have extra child: {len(population.get_all_people_exhibiting_trait(const.MORE_LIKELY_FOR_EXTRA_CHILD_GENE))}")
    print(f"People with blonde hair: {len(population.get_all_people_exhibiting_trait(const.HAS_BLONDE_HAIR_GENE))}")
    print(f"People who cannot reproduce: {len(population.get_all_people_exhibiting_trait(const.CANNOT_REPRODUCE_GENE))}")
    print(f"People who die early: {len(population.get_all_people_exhibiting_trait(const.PREMATURE_DEATH_GENE))}")

    plt.xlabel('Generation number')
    plt.title(f"Starting avg death age: {average_person_death_age}, population mutation proportion: {population_proportion_mutated}")
    plt.plot(young_people, color='b', label='young-people')
    plt.plot(old_people, color='r', label='old-people')
    plt.plot(population_sizes_at_varying_generations, color='g', label='population-size')
    plt.plot(average_death_ages, color='y', label='average-death-ages')
    plt.legend()
    plt.show()
    plt.ylabel('Ratio of bad traits population vs population')
    plt.plot(people_with_bad_traits_ratio, color='r', label='people-who-cannot-reproduce')
    plt.plot(people_who_died_prematurely_ratio, color='g', label='premature-age-death')
    plt.show()

    person_has_recessive_gene = True
    person_has_dominant_gene = False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
