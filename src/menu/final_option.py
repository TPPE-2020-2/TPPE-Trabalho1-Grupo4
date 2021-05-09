from .menu_options import MenuOptions

class FinalOption(MenuOptions):
    def choose_option(self):
        final = input("Nome do Nó Final: ")
        self.act.elements.create_final(final)