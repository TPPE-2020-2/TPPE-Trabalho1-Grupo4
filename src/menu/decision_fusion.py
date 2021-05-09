from .decision_type_options import DecisionType

class DecisionFusion(DecisionType):
    def choose_option(self):
        merge_name = input("Nome do Nó de Fusão: ")
        self.decision.create_merge(merge_name)