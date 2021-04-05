from .lifelines import Lifelines
from .fragments import Fragments

from .excepts import EmptyOptionalFragment


class SequenceDiagrams():

    def __init__(self):
        self.sequence_diagrams = []
        self.lifelines = []
        self.fragments = []

    def create_and_persist_lifelines(self, lifeline_name):
        lifeline = Lifelines(lifeline_name)
        self.lifelines.append(lifeline)

    def create_and_persist_fragments(
        self, fragment_name, fragment_represented
    ):

        if self.sequence_diagram_exists(fragment_represented) is True:
            fragment = Fragments(fragment_name, fragment_represented)
            self.fragments.append(fragment)

        else:
            raise EmptyOptionalFragment

    def lifeline_exists(self, name):
        for i in self.lifelines:
            if i.name == name:
                return True

        return False

    def sequence_diagram_exists(self, name):
        for i in self.sequence_diagrams:
            if i.name == name:
                return True

        return False

    def create_single_sequence_diagram(self, sequence_diagram):
        self.sequence_diagrams.append(sequence_diagram)

    def create_lifelines_xml(self, f):
        f.write("\t<Lifelines>\n")

        for lifeline in self.lifelines:
            lifeline.lifeline_to_xml(f)

        f.write("\t</Lifelines>\n")

    def create_fragments_xml(self, f):
        f.write("\t<Fragments>\n")

        for fragment in self.fragments:
            fragment.fragments_to_xml(f)

        f.write("\t</Fragments>\n")

    def create_sequence_diagrams_xml(self, f):
        for diagram in self.sequence_diagrams:

            m_count = 0
            f_count = 0

            f.write(
                "\t<SequenceDiagram name=" +
                "\"{}\" guard_condition=\"{}\">\n".format(
                    diagram.name, diagram.guard
                )
            )

            for i in diagram.elements:

                if i == 0:
                    diagram.xml_message_by_position(m_count, f)
                    m_count += 1

                elif i == 1:
                    diagram.xml_fragment_by_position(f_count, f)
                    f_count += 1

            f.write("\t</SequenceDiagram>\n")

    def create_xml(self, activity):
        f = open("sequence_diagram_activity_{}.xml".format(activity), "w")

        f.write("<SequenceDiagrams>\n")

        self.create_lifelines_xml(f)
        self.create_fragments_xml(f)
        self.create_sequence_diagrams_xml(f)

        f.write("</SequenceDiagrams>\n")

        f.close()
