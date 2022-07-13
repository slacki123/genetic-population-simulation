import math
import random

import numpy as np

import constants
from person import Person


class Population:
    def __init__(self, initial_size: int, average_person_death_age: int, average_number_of_children: float):
        self.average_number_of_children = average_number_of_children
        self.average_person_death_age = average_person_death_age
        self.population = self.generate_population(initial_size)
        self.resource_factor = 0

    def generate_population(self, initial_size):
        population = []
        for i in range(0, initial_size):
            person_death_age = np.random.normal(self.average_person_death_age, 1)
            population.append(
                Person.get_random_person(
                    death_age=person_death_age,
                    age=random.uniform(0, person_death_age),
                    max_offspring=np.random.normal(self.average_number_of_children, 1)
                )
            )
        return population

    def eliminate_persons_exhibiting_trait(self, trait: str):
        self.population = [person for person in self.population if not person.get_gene(trait).exhibits_trait()]

    def reproduce_generation(self):
        all_reproductive_females = self.get_all_reproductive_females()
        all_reproductive_males = self.get_all_reproductive_males()

        for female in all_reproductive_females:
            # Each female mates with a random male this generation
            number_of_males = len(all_reproductive_males)
            if number_of_males == 0:
                continue
            # TODO: introduce male competition and female selection based on male's resources here
            random_male_index = random.randint(0, number_of_males - 1)
            random_male = all_reproductive_males[random_male_index]
            offspring = random_male.mate(female)
            self.population.append(offspring)

    def add_some_genetic_mutations(self, population_proportion: float):
        if population_proportion <= 0 or population_proportion > 1:
            raise Exception("Population proportion must be between 0 and 1")
        people_to_mutate = int(self.size() * population_proportion)
        for i in range(len(self.population)):
            self.population[i].randomly_mutate_genes()
            if i > people_to_mutate:
                return

    def age_population(self, increment_years=1):
        for person in self.population:
            person.increment_age(increment_years)

    def eliminate_old_persons(self):
        self.population = [person for person in self.population if not person.died_of_old_age()]

    def size(self):
        return len(self.population)

    ### Getters

    def get_all_people_exhibiting_trait(self, trait):
        return [person for person in self.population if person.get_gene(trait).exhibits_trait()]

    def get_all_reproductive_females(self):
        return [person for person in self.population
                if not person.is_male_sex
                and person.max_reproductive_age > person.age > person.reproductive_age
                and person.max_offspring > person.number_of_offspring
                and not person.exhibits_gene_trait(constants.CANNOT_REPRODUCE_GENE)]

    def get_all_reproductive_males(self):
        return [person for person in self.population
                if person.is_male_sex
                and person.max_reproductive_age > person.age > person.reproductive_age
                and person.max_offspring > 0
                and not person.exhibits_gene_trait(constants.CANNOT_REPRODUCE_GENE)
                ]

    def get_all_people_older_than(self, age):
        return [person for person in self.population if person.age > age]

    def get_all_people_younger_than(self, age):
        return [person for person in self.population if person.age < age]
