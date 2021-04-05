class ActivityTransitions():

    def __init__(self, transition_name, transition_prob):
        self.transition_name = transition_name
        self.transition_prob = transition_prob

    def transition_to_xml(self, f, is_decision):
        if is_decision:
            f.write(
                "\t\t\t\t\t<Transition name=\"{}\" prob=\"{}\"/>\n".format(
                    self.transition_name, self.transition_prob
                )
            )

        else:
            f.write(
                "\t\t<Transition name=\"{}\" prob=\"{}\"/>\n".format(
                    self.transition_name, self.transition_prob
                )
            )
