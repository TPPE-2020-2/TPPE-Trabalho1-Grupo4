from .sequence_diagrams import SequenceDiagrams
from .sequence_diagram_block import SequenceDiagramBlock
import os

from .excepts import EmptyGuardConditionException, MessageFormatException


def create_sequence_diagram(activity):
    seq = SequenceDiagrams()
    while(1):
        os.system("clear")

        option = int(input(
            "Criando Diagrama de Sequencia da Atividade {}\n".format(activity) +  #
            "1 - Lifeline\n" +
            "2 - Fragmentos\n" +
            "3 - Diagrama de Sequência\n" +
            "4 - Sair\n" +
            "-> "
        ))

        if option == 1:
            lifeline_name = input("Nome da Lifeline: ")
            seq.create_and_persist_lifelines(lifeline_name)

        elif option == 2:
            fragment_name = input("Nome do Fragmento: ")
            fragment_represented = input("Fragmento representado por: ")

            seq.create_and_persist_fragments(
                fragment_name, fragment_represented
            )

        elif option == 3:
            name = input("Nome do Diagrama: ")  #
            guard_condition = input("Condição de Guarda: ")  #

            if bool(guard_condition) is False:
                raise EmptyGuardConditionException

            sequence_diagram = SequenceDiagramBlock(name, guard_condition)

            while True:
                os.system("clear")

                option1 = int(input(
                    "Deseja escolher inserir\n" +  #
                    "1 - Mensagem\n" +
                    "2 - Fragmento\n" +
                    "3 - Sair\n" +
                    "-> "
                ))

                if option1 == 1:
                    m_name = input("Nome da Mensagem: ")
                    m_prob = input("Probabilidade da Mensagem: ")

                    source_lifeline = input("Lifeline de Origem: ")
                    target_lifeline = input("Lifeline Alvo: ")

                    if (
                        not seq.lifeline_exists(source_lifeline) and
                        not seq.lifeline_exists(target_lifeline)
                    ):
                        raise MessageFormatException

                    sequence_diagram.persist_messages(
                        m_name, m_prob, source_lifeline, target_lifeline
                    )

                    sequence_diagram.elements_update(option - 1)

                elif option1 == 2:
                    fragment_name = input("Nome do Fragmento: ")

                    sequence_diagram.persist_fragments(fragment_name)
                    sequence_diagram.elements_update(option - 1)

                else:
                    break

            seq.create_single_sequence_diagram(sequence_diagram)

        else:
            seq.create_xml(activity)
            break
