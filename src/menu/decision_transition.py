from .decision_type_options import DecisionType

class DecisionTransition(DecisionType):
    def choose_option(self):
        transition_name = input(
            "Nome da Transição: "
        )

        transition_prob = input(
            "Probabilidade da Transição: "
        )

        self.decision.create_transition(
            transition_name, transition_prob
        )