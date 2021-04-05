from .transitions import ActivityTransitions


class DecisionStream():

    def __init__(self):
        self.transitions = []

        self.merge_node = None

        self.activity_node = []

        self.elements = []

    def create_activity(self, activity_name):
        self.activity_node.append(activity_name)
        self.elements.append(0)

    def create_transition(self, transition_name, transition_prob):
        transition = ActivityTransitions(transition_name, transition_prob)
        self.transitions.append(transition)

    def create_merge(self, merge_name):
        self.merge_node = merge_name
        self.elements.append(1)

    def decision_stream_to_xml(self, f, k):
        f.write("\t\t\t<DecisionStream count=\"{}\">\n".format(k+1))

        a_count = 0
        m_count = 0

        for i in self.elements:

            if i == 0:
                f.write("\t\t\t\t<Activity name=\"{}\"/>\n".format(
                    self.activity_node[a_count]
                ))

                a_count += 1

            elif i == 1:
                f.write("\t\t\t\t<MergeNode name=\"{}\"/>\n".format(
                    self.merge_node[m_count]
                ))

                m_count += 1

        f.write("\t\t\t\t<DecisionStreamTransitions>\n")

        for transition in self.transitions:
            transition.transition_to_xml(f, True)

        f.write("\t\t\t\t</DecisionStreamTransitions>\n")
        f.write("\t\t\t</DecisionStream>\n")
