import random

import constants as const
import numpy as np

from person import Person


class Population:
    def __init__(self, initial_size: int, average_person_death_age: int):
        self.average_person_death_age = average_person_death_age
        self.population = self.generate_population(initial_size)

    def generate_population(self, initial_size):
        population = []
        for i in range(0, initial_size):
            population.append(
                Person.get_random_person(
                    death_age=random.randint(self.average_person_death_age-5, self.average_person_death_age+5),
                    age=random.randint(0, self.average_person_death_age+5),
                    max_offspring=round(np.random.gamma(3.5, 0.5))
                )
            )
        return population

    def eliminate_persons_exhibiting_trait(self, trait: str):
        self.population = [person for person in self.population if not person.get_gene(trait).exhibits_trait()]

    def eliminate_persons_with_bad_genes(self):
        self.eliminate_persons_exhibiting_trait(const.CANNOT_REPRODUCE_GENE)

    def reproduce_generation(self):
        all_females = self.get_all_females()
        all_males = self.get_all_males()

        all_offspring = []
        for female in all_females:
            # Skip if this female already had her max number of offspring she can manage
            if female.number_of_offspring >= female.max_offspring or female.reproductive_age > female.age:
                continue
            # Each female mates with a random male this generation
            random_male_index = random.randint(0, len(all_males) - 1)
            random_male = all_males[random_male_index]
            offspring = random_male.mate(female)
            all_offspring.append(offspring)

        self.population = self.population + all_offspring

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

    def get_all_females(self):
        return [person for person in self.population if not person.is_male_sex]

    def get_all_males(self):
        return [person for person in self.population if person.is_male_sex]

    def get_all_people_older_than(self, age):
        return [person for person in self.population if person.age > age]

    def get_all_people_younger_than(self, age):
        return [person for person in self.population if person.age < age]
