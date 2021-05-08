from sequence.sequence_diagrams import SequenceDiagrams
from sequence.lifelines import Lifelines
from sequence.fragments import Fragments
from sequence.sequence_diagram_block import SequenceDiagramBlock


def test_sequence_diagram():
    obj = SequenceDiagrams()
    assert [] == obj.sequence_diagrams


def test_sequence_diagram2():
    obj = SequenceDiagrams()
    assert [] == obj.sequence_diagrams


def test_sequence_diagram3():
    obj = SequenceDiagrams()
    assert [] == obj.sequence_diagrams


def test_create_lifeline():
    lf = Lifelines("l1")
    assert 'l1' == lf.name


def test_create_lifeline2():
    lf = Lifelines("l2")
    assert 'l2' == lf.name


def test_create_lifeline3():
    lf = Lifelines("l3")
    assert 'l3' == lf.name


def test_sequence_diagram_of_fragment():
    obj = SequenceDiagrams()
    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')

    obj.create_single_sequence_diagram(seq_diagram)

    assert 'sq1' == obj.sequence_diagrams[0].name
    assert '[guard]' == obj.sequence_diagrams[0].guard


def test_sequence_diagram_of_fragment2():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    seq_diagram_2 = SequenceDiagramBlock('sq2', '[guard2]')

    obj.create_single_sequence_diagram(seq_diagram)
    obj.create_single_sequence_diagram(seq_diagram_2)

    assert 'sq1' == obj.sequence_diagrams[0].name
    assert '[guard]' == obj.sequence_diagrams[0].guard

    assert 'sq2' == obj.sequence_diagrams[1].name
    assert '[guard2]' == obj.sequence_diagrams[1].guard


def test_sequence_diagram_of_fragment3():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    seq_diagram_2 = SequenceDiagramBlock('sq2', '[guard2]')
    seq_diagram_3 = SequenceDiagramBlock('sq3', '[guard3]')

    obj.create_single_sequence_diagram(seq_diagram)
    obj.create_single_sequence_diagram(seq_diagram_2)
    obj.create_single_sequence_diagram(seq_diagram_3)

    assert 'sq1' == obj.sequence_diagrams[0].name
    assert '[guard]' == obj.sequence_diagrams[0].guard

    assert 'sq2' == obj.sequence_diagrams[1].name
    assert '[guard2]' == obj.sequence_diagrams[1].guard

    assert 'sq3' == obj.sequence_diagrams[2].name
    assert '[guard3]' == obj.sequence_diagrams[2].guard


def test_create_fragments():
    fragment = Fragments('f1', 'sq1')
    assert 'f1' == fragment.name
    assert 'sq1' == fragment.represented


def test_create_fragments2():
    fragment = Fragments('f1', 'sq1')
    fragment2 = Fragments('f2', 'sq2')
    assert 'f1' == fragment.name
    assert 'sq1' == fragment.represented
    assert 'f2' == fragment2.name
    assert 'sq2' == fragment2.represented


def test_create_fragments3():
    fragment = Fragments('f1', 'sq1')
    fragment2 = Fragments('f2', 'sq2')
    fragment3 = Fragments('f3', 'sq3')
    assert 'f1' == fragment.name
    assert 'sq1' == fragment.represented
    assert 'f2' == fragment2.name
    assert 'sq2' == fragment2.represented
    assert 'f3' == fragment3.name
    assert 'sq3' == fragment3.represented


def test_persist_messages():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)
    lf = Lifelines('l1')
    obj.append_lifeline(lf)


    obj.sequence_diagrams[0].persist_messages('m1', '0.99', 'l1', 'l1')

    assert 'm1' == obj.sequence_diagrams[0].messages[0].name
    assert '0.99' == obj.sequence_diagrams[0].messages[0].prob
    assert 'l1' == obj.sequence_diagrams[0].messages[0].source_lifeline
    assert 'l1' == obj.sequence_diagrams[0].messages[0].target_lifeline


def test_persist_messages2():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    lf = Lifelines('l1')
    lf2 = Lifelines('l2')
    obj.append_lifeline(lf)
    obj.append_lifeline(lf2)

    obj.sequence_diagrams[0].persist_messages('m1', '0.99', 'l1', 'l1')
    obj.sequence_diagrams[0].persist_messages('m2', '0.01', 'l1', 'l2')

    assert 'm1' == obj.sequence_diagrams[0].messages[0].name
    assert '0.99' == obj.sequence_diagrams[0].messages[0].prob
    assert 'l1' == obj.sequence_diagrams[0].messages[0].source_lifeline
    assert 'l1' == obj.sequence_diagrams[0].messages[0].target_lifeline

    assert 'm2' == obj.sequence_diagrams[0].messages[1].name
    assert '0.01' == obj.sequence_diagrams[0].messages[1].prob
    assert 'l1' == obj.sequence_diagrams[0].messages[1].source_lifeline
    assert 'l2' == obj.sequence_diagrams[0].messages[1].target_lifeline


def test_persist_messages3():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    lf = Lifelines('l1')
    lf2 = Lifelines('l2')
    obj.append_lifeline(lf)
    obj.append_lifeline(lf2)

    obj.sequence_diagrams[0].persist_messages('m1', '0.99', 'l1', 'l1')
    obj.sequence_diagrams[0].persist_messages('m2', '0.01', 'l1', 'l2')
    obj.sequence_diagrams[0].persist_messages('m3', '0.80', 'l2', 'l2')

    assert 'm1' == obj.sequence_diagrams[0].messages[0].name
    assert '0.99' == obj.sequence_diagrams[0].messages[0].prob
    assert 'l1' == obj.sequence_diagrams[0].messages[0].source_lifeline
    assert 'l1' == obj.sequence_diagrams[0].messages[0].target_lifeline

    assert 'm2' == obj.sequence_diagrams[0].messages[1].name
    assert '0.01' == obj.sequence_diagrams[0].messages[1].prob
    assert 'l1' == obj.sequence_diagrams[0].messages[1].source_lifeline
    assert 'l2' == obj.sequence_diagrams[0].messages[1].target_lifeline

    assert 'm3' == obj.sequence_diagrams[0].messages[2].name
    assert '0.80' == obj.sequence_diagrams[0].messages[2].prob
    assert 'l2' == obj.sequence_diagrams[0].messages[2].source_lifeline
    assert 'l2' == obj.sequence_diagrams[0].messages[2].target_lifeline


def test_persist_fragments():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    obj.sequence_diagrams[0].persist_fragments('f1')

    assert 'f1' == obj.sequence_diagrams[0].fragments[0]


def test_persist_fragments2():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    obj.sequence_diagrams[0].persist_fragments('f1')
    obj.sequence_diagrams[0].persist_fragments('f2')

    assert 'f1' == obj.sequence_diagrams[0].fragments[0]
    assert 'f2' == obj.sequence_diagrams[0].fragments[1]


def test_persist_fragments3():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    obj.sequence_diagrams[0].persist_fragments('f1')
    obj.sequence_diagrams[0].persist_fragments('f2')
    obj.sequence_diagrams[0].persist_fragments('f3')

    assert 'f1' == obj.sequence_diagrams[0].fragments[0]
    assert 'f2' == obj.sequence_diagrams[0].fragments[1]
    assert 'f3' == obj.sequence_diagrams[0].fragments[2]
