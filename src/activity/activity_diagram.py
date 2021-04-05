from .elements import ActivityElements
from .transitions import ActivityTransitions


class ActivityDiagram():

    def __init__(self, name):
        self.name = name
        self.elements = None
        self.transitions = []

    def create_initial_node(self, name):
        start_node = name
        self.elements = ActivityElements(start_node)

    def create_transitions(self, name, prob):
        transition = ActivityTransitions(name, prob)
        self.transitions.append(transition)

    def create_xml(self):
        f = open("diagram.xml", "w")

        f.write("<ActivityDiagram name=\"{}\">\n".format(self.name))

        self.elements.create_elements_xml(f)

        f.write("\t<ActivityDiagramTransitions>\n")

        for transition in self.transitions:
            transition.transition_to_xml(f, False)

        f.write("\t</ActivityDiagramTransitions>\n")
        f.write("</ActivityDiagram>")

        f.close()
