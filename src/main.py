from activity.activity_diagram import ActivityDiagram
from activity.decision_node import DecisionStream
from activity.exceptions import ActivityRepresentationException
from sequence.create_sequence import create_sequence_diagram
from menu.menu_options import MenuOptions
from menu.transitions_options import TransitionsOptions
from menu.elements_options import ElementsOptions
import os


if __name__ == "__main__":
    opt = input("Deseja criar um novo Diagrama de Atividades (s/n): ")

    if opt[0].lower() == "s":
        name = input("Nome do Diagrama: ")

        act = ActivityDiagram(name)

        while (1):
            os.system("clear")

            option = int(input(
                "-- Criação do Diagrama de Atividades --\n" +
                "1 - Inserir Elementos\n" +
                "2 - Inserir Transição\n" +
                "3 - Finalizar Diagrama de Atividade\n" +
                "-> "
            ))

            if option == 1:
                obj = ElementsOptions(act)
            
            elif option == 2:
                obj = TransitionsOptions(act)

            else:
                act.create_xml()
                break

            obj.choose_option()

        created = [False for i in range(len(act.elements.activity_name))]

        while True:
            os.system("clear")
            print("-- Criação dos Diagramas de Sequencia ")

            activities = [name for name in act.elements.activity_name]

            for i in range(len(activities)):
                print(
                    "{} - Diagrama de Sequencia da Atividade {}"
                    .format(i+1, activities[i])
                )

            print("{} - Sair".format(len(activities)+1))
            option = int(input("-> "))

            if option >= len(activities) + 1:
                for i in range(len(activities)):
                    if not created[i]:
                        raise ActivityRepresentationException
                break

            created[option-1] = True
            create_sequence_diagram(activities[option-1])
    else:
        print("Saindo...\n")
