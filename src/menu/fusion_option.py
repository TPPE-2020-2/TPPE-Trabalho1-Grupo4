from .menu_options import MenuOptions

class FusionOption(MenuOptions):
    def choose_option(self):
        merge = input("Nome do Nó de Fusão: ")
        self.act.elements.create_merge(merge)