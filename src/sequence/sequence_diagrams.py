from .lifelines import Lifelines
from .fragments import Fragments

from .excepts import EmptyOptionalFragment


class SequenceDiagrams():

    def __init__(self):
        self.sequence_diagrams = []
        self.lifelines = []
        self.fragments = []

    def append_lifeline(self, lifeline):
        self.lifelines.append(lifeline)

    def append_fragment(self, fragment):
        if self.sequence_diagram_exists(fragment.represented) is True:
            self.fragments.append(fragment)
        else:
            raise EmptyOptionalFragment

    def lifeline_exists_in_Sequence_Diagram(self, name):
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

