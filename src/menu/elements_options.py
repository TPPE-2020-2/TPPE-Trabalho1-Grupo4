from .menu_options import MenuOptions
from .decision_option import DecisionOption
from .final_option import FinalOption
from .fusion_option import FusionOption
from .activity_option import ActivityOption
import os


class ElementsOptions(MenuOptions):

    def choose_option(self):
        start_node = input("Nome do Nó Inicial: ")
        self.act.create_initial_node(start_node)

        while (1):
            os.system("clear")

            option1 = int(input(
                "-- Inserir Elemento no Diagrama de Atividades --\n" +
                "1 - Atividade\n" +
                "2 - Nó de Decisão\n" +
                "3 - Nó de Fusão\n" +
                "4 - Nó Final\n" +
                "5 - Sair\n" +
                "-> "
            ))

            if option1 == 1:
                obj = ActivityOption(self.act)

            elif option1 == 2:
                obj = DecisionOption(self.act)

            elif option1 == 3:
                obj = FusionOption(self.act)

            elif option1 == 4:
                obj = FinalOption(self.act)

            else:
                break

            obj.choose_option()