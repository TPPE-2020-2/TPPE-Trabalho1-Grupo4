class Fragments:

    def __init__(self, name, represented):
        self.name = name
        self.represented = represented

    def fragments_to_xml(self, f):
        f.write("\t\t<Optional name=\"{}\" representedBy=\"{}\"/>\n".format(
            self.name, self.represented
        ))
