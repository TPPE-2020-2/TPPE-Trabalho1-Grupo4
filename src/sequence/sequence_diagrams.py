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

    def compareNames(self, vector_obj, name):
        for obj in vector_obj:
            if obj.name == name:
                return True
        return False

    def lifeline_exists_in_Sequence_Diagram(self, name):
        return self.compareNames(self.lifelines,name)

    def sequence_diagram_exists(self, name):
        return self.compareNames(self.sequence_diagrams,name)
    
    def create_single_sequence_diagram(self, sequence_diagram):
        self.sequence_diagrams.append(sequence_diagram)

