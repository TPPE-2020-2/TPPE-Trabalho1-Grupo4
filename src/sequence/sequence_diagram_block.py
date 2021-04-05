from .message import Messages

from .excepts import MessageFormatException


class SequenceDiagramBlock:

    def __init__(self, name, guard):
        self.name = name
        self.guard = guard

        self.messages = []
        self.fragments = []
        self.elements = []

    def persist_messages(
        self, m_name, m_prob, source_lifeline, target_lifeline
    ):
        if (
            bool(m_name) and bool(source_lifeline) and
            bool(target_lifeline) and bool(m_prob) and m_prob[0] != '-'
        ) is False:
            raise MessageFormatException

        message = Messages(m_name, m_prob, source_lifeline, target_lifeline)
        self.messages.append(message)

    def persist_fragments(self, name):
        self.fragments.append(name)

    def elements_update(self, tp):
        self.elements.append(tp)

    def xml_message_by_position(self, i, f):
        self.messages[i].message_to_xml(f)

    def xml_fragment_by_position(self, i, f):
        f.write("\t\t<Fragment name=\"{}\">\n".format(self.fragments[i]))
