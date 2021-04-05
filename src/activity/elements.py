from .exceptions import ActivityDiagramRuleException


class ActivityElements():

    def __init__(self, start_node):
        self.start_node = start_node

        self.activity_name = []

        self.decision_node = [[]]
        self.decision_node_number = 0

        self.merge_node = []
        self.final_node = None

        self.elements_order = []

    def create_activity(self, name):
        activity = name
        self.activity_name.append(activity)

        self.elements_order.append(0)

    def initiate_decision(self, streams):
        self.decision_node = [[] for i in range(streams)]

    def create_decision(self, decision):
        self.decision_node[self.decision_node_number].append(decision)

    def aux_decision(self):
        self.elements_order.append(1)
        self.decision_node_number += 1

    def create_merge(self, name):
        merge = name
        self.merge_node.append(merge)

        self.elements_order.append(2)

    def create_final(self, name):
        if self.final_node is not None:
            raise ActivityDiagramRuleException

        self.final_node = name
        self.elements_order.append(3)

    def create_elements_xml(self, f):
        f.write("\t<ActivityDiagramElements>\n")
        f.write("\t\t<StartNode name=\"{}\"/>\n".format(self.start_node))

        a_count = 0
        d_count = 0
        m_count = 0

        if self.final_node is None:
            raise ActivityDiagramRuleException

        for i in self.elements_order:

            if i == 0:
                f.write("\t\t<Activity name=\"{}\"/>\n".format(
                    self.activity_name[a_count]
                ))

                a_count += 1

            elif i == 1:
                j = 0

                f.write("\t\t<DecisionNode>\n")

                for decision_stream in self.decision_node[d_count]:
                    decision_stream.decision_stream_to_xml(f, j)
                    j += 1

                f.write("\t\t</DecisionNode>\n")
                d_count += 1

            elif i == 2:
                f.write("\t\t<MergeNode name=\"{}\"/>\n".format(
                    self.merge_node[m_count]
                ))

                m_count += 1

            elif i == 3:
                f.write("\t\t<FinalNode name=\"{}\"/>\n".format(
                    self.final_node
                ))

        f.write("\t</ActivityDiagramElements>\n")
