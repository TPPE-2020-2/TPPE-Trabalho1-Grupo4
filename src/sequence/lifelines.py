class Lifelines:

    def __init__(self, name):
        self.name = name

    def lifeline_to_xml(self, f):
        f.write("\t\t<Lifeline name=\"{}\"/>\n".format(self.name))
