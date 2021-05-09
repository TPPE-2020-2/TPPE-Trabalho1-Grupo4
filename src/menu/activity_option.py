from .menu_options import MenuOptions

class ActivityOption(MenuOptions):
    def choose_option(self):
        activity_name = input("Nome da Atividade: ")
        self.act.elements.create_activity(activity_name)