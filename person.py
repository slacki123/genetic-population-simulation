import random
from person_gene import PersonGene
import constants as const
import numpy as np


class Person:
    def __init__(
            self,
            genes: dict[str, PersonGene],
            age: int,
            death_age: int,
            max_offspring: int):
        self.genes: dict[str, PersonGene] = genes
        self.is_male_sex = random.choice([True, False])
        self.age = age
        self.death_age = death_age
        self.number_of_offspring = round((age / death_age) * max_offspring)
        self.max_offspring = max_offspring  # Only for females
        self.reproductive_age = random.randint(12, 16)  # A society where children have children

    def __repr__(self):
        return str(self.__dict__)

    def increment_number_of_offspring(self):
        self.number_of_offspring = self.number_of_offspring + 1

    def randomly_mutate_genes(self):
        for (gene_name, gene) in self.genes.items():
            self.genes[gene_name].randomly_mutate()

    def mate(self, person):
        """
        Mate with a parter of opposite sex
        :param person: The partner
        :return:
        """
        if self.is_male_sex and person.is_male_sex:
            raise Exception("Cannot make children having the same sex... (No need to get triggered, it's a fact)")

        offspring_genes = {}
        for (gene_name, gene) in self.genes.items():
            parent_1_gene: PersonGene = person.genes[gene_name]
            parent_2_gene: PersonGene = self.genes[gene_name]
            parent_1_selected_gene = parent_1_gene.select_either_gene_randomly()
            parent_2_selected_gene = parent_2_gene.select_either_gene_randomly()
            offspring_gene = PersonGene(gene_name, parent_1_selected_gene, parent_2_selected_gene)
            offspring_genes[gene_name] = offspring_gene

        max_offspring_offspring = round(np.random.gamma(4, 0.5))
        death_age = round((person.death_age + self.death_age) / 2)
        offspring = Person(offspring_genes, 0, death_age, max_offspring_offspring)
        self.increment_number_of_offspring()
        person.increment_number_of_offspring()
        # print(f"OMG It's a {'boy' if is_new_offspring_male else 'girl'}!!!")
        return offspring

    def get_gene(self, trait) -> PersonGene:
        return self.genes[trait]

    def increment_age(self, num_years=1):
        self.age += num_years

    def died_of_old_age(self):
        return self.age > self.death_age

    def person_exhibits_combined_trait(self, exhibiting_gene_configuration: dict[str, bool]):
        pass

    @staticmethod
    def get_random_person(death_age=100, age=0, max_offspring=5):
        person_genes = {
            const.CANNOT_REPRODUCE_GENE: PersonGene.get_random_gene(const.CANNOT_REPRODUCE_GENE),
            const.HAS_BLUE_EYES_GENE: PersonGene.get_random_gene(const.HAS_BLUE_EYES_GENE),
            const.HAS_BLONDE_HAIR_GENE: PersonGene.get_random_gene(const.HAS_BLONDE_HAIR_GENE),
            const.EARLY_BALDING_GENE: PersonGene.get_random_gene(const.EARLY_BALDING_GENE)
            # Add more genes of choice
        }
        return Person(
            person_genes,
            age=age,
            death_age=death_age,
            max_offspring=max_offspring)
