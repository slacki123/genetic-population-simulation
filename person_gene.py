import random


class PersonGene:
    def __init__(self, gene_name: str, is_gene_a_recessive: bool, is_gene_b_recessive: bool):
        self.gene_name = gene_name
        self.is_gene_a_recessive = is_gene_a_recessive
        self.is_gene_b_recessive = is_gene_b_recessive

    def exhibits_trait(self):
        return self.is_gene_a_recessive and self.is_gene_b_recessive

    def randomly_mutate(self):
        self.is_gene_a_recessive = random.choice([True, False])
        self.is_gene_b_recessive = random.choice([True, False])

    def select_either_gene_randomly(self):
        """
        Select gene A or B part for reproduction
        :return:
        """
        return random.choice([self.is_gene_a_recessive, self.is_gene_b_recessive])

    @staticmethod
    def get_random_gene(gene_name):
        return PersonGene(
            gene_name=gene_name,
            is_gene_a_recessive=random.choice([True, False]),
            is_gene_b_recessive=random.choice([True, False])
        )

    def __repr__(self):
        return str(self.__dict__)
