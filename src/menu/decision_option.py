from .menu_options import MenuOptions
from .decision_fusion import DecisionFusion
from .decision_transition import DecisionTransition
from .decision_activity import DecisionActivity
import sys
from activity import decision_node
import os

class DecisionOption(MenuOptions):
    def choose_option(self):
        streams = int(input("Quantidade de Fluxos: "))

        for i in range(streams):
            decision = decision_node.DecisionStream()

            while True:
                os.system("clear")

                option2 = int(input(
                    "-- Criação do Fluxo de Decisão " +
                    "{} --\n".format(i+1) +
                    "1 - Inserir Atividade\n" +
                    "2 - Inserir Transição\n" +
                    "3 - Inserir Nó de Fusão / Sair\n" +
                    "4 - Sair\n" +
                    "-> "
                ))

                if option2 == 1:
                    obj = DecisionActivity(decision)

                elif option2 == 2:
                    obj = DecisionTransition(decision)

                elif option2 == 3:
                    obj = DecisionFusion(decision)
                    obj.choose_option()
                    break

                elif option2 == 4:
                    break
                
                obj.choose_option()

            self.act.elements.create_decision(decision)

        self.act.elements.aux_decision()