class Messages:

    def __init__(self, name, prob, source_lifeline, target_lifeline):
        self.name = name
        self.prob = prob

        self.source_lifeline = source_lifeline
        self.target_lifeline = target_lifeline

    def message_to_xml(self, f):
        f.write(
            "\t\t<Message name=" +
            "\"{}\" prob=\"{}\" source=\"{}\" target=\"{}\"/>\n".format(
                self.name, self.prob, self.source_lifeline,
                self.target_lifeline
            )
        )
