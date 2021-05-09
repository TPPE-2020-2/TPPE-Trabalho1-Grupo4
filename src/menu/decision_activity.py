from .decision_type_options import DecisionType

class DecisionActivity(DecisionType):
    def choose_option(self):
        activity_name = input(
            "Nome da Atividade: "
        )
        self.decision.create_activity(activity_name)