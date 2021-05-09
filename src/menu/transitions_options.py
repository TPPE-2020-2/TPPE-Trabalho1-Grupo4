from .menu_options import MenuOptions

class TransitionsOptions(MenuOptions):
    def choose_option(self):
        name = input("Nome da Transição: ")
        prob = float(input("Probabilidade da Transição: "))

        self.act.create_transitions(name, prob)