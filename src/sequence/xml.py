import time
class XML:

    def __init__(self, lifeline, fragments, sequence_diagrams, activity):
        self.arquivo = None
        self.lifelines = lifeline
        self.fragments = fragments
        self.sequence_diagrams = sequence_diagrams
        self.activity_name = activity


    def create_lifelines_xml(self):
        self.arquivo.write("\t<Lifelines>\n")
        for lifeline in self.lifelines:
            lifeline.lifeline_to_xml(self.arquivo)
        self.arquivo.write("\t</Lifelines>\n")


    def create_fragments_xml(self):
        self.arquivo.write("\t<Fragments>\n")
        for fragment in self.fragments:
            fragment.fragments_to_xml(self.arquivo)
        self.arquivo.write("\t</Fragments>\n")

    def create_sequence_diagrams_xml(self):
        for diagram in self.sequence_diagrams:
            m_count = 0; f_count = 0

            self.arquivo.write(
                "\t<SequenceDiagram name=" +
                "\"{}\" guard_condition=\"{}\">\n".format(
                    diagram.name, diagram.guard
                )
            )
            
            for i in diagram.elements:
                if i == 0:
                    diagram.xml_message_by_position(m_count, self.arquivo)
                    m_count += 1

                elif i == 1:
                    diagram.xml_fragment_by_position(f_count, self.arquivo)
                    f_count += 1


            self.arquivo.write("\t</SequenceDiagram>\n")

    def create_xml(self):
        self.arquivo = open("sequence_diagram_activity_{}.xml".format(self.activity_name), "w")
        self.arquivo.write("<SequenceDiagrams>\n")
        self.create_lifelines_xml()
        self.create_fragments_xml()
        self.create_sequence_diagrams_xml()
        self.arquivo.write("</SequenceDiagrams>\n")
        self.arquivo.close()

        
        
