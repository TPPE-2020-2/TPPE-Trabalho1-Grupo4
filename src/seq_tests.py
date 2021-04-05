from sequence.sequence_diagrams import SequenceDiagrams
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
    obj = SequenceDiagrams()
    obj.create_and_persist_lifelines('l1')
    assert 'l1' == obj.lifelines[0].name


def test_create_lifeline2():
    obj = SequenceDiagrams()
    obj.create_and_persist_lifelines('l2')
    assert 'l2' == obj.lifelines[0].name


def test_create_lifeline3():
    obj = SequenceDiagrams()
    obj.create_and_persist_lifelines('l3')
    assert 'l3' == obj.lifelines[0].name


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
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    obj.create_and_persist_fragments('f1', 'sq1')

    assert 'f1' == obj.fragments[0].name


def test_create_fragments2():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    seq_diagram_2 = SequenceDiagramBlock('sq2', '[guard2]')
    obj.create_single_sequence_diagram(seq_diagram_2)

    obj.create_and_persist_fragments('f1', 'sq1')
    obj.create_and_persist_fragments('f2', 'sq2')

    assert 'f1' == obj.fragments[0].name
    assert 'f2' == obj.fragments[1].name


def test_create_fragments3():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    seq_diagram_2 = SequenceDiagramBlock('sq2', '[guard2]')
    obj.create_single_sequence_diagram(seq_diagram_2)

    seq_diagram_3 = SequenceDiagramBlock('sq3', '[guard3]')
    obj.create_single_sequence_diagram(seq_diagram_3)

    obj.create_and_persist_fragments('f1', 'sq1')
    obj.create_and_persist_fragments('f2', 'sq2')
    obj.create_and_persist_fragments('f3', 'sq3')

    assert 'f1' == obj.fragments[0].name
    assert 'f2' == obj.fragments[1].name
    assert 'f3' == obj.fragments[2].name


def test_persist_messages():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    obj.create_and_persist_lifelines('l1')

    obj.sequence_diagrams[0].persist_messages('m1', '0.99', 'l1', 'l1')

    assert 'm1' == obj.sequence_diagrams[0].messages[0].name
    assert '0.99' == obj.sequence_diagrams[0].messages[0].prob
    assert 'l1' == obj.sequence_diagrams[0].messages[0].source_lifeline
    assert 'l1' == obj.sequence_diagrams[0].messages[0].target_lifeline


def test_persist_messages2():
    obj = SequenceDiagrams()

    seq_diagram = SequenceDiagramBlock('sq1', '[guard]')
    obj.create_single_sequence_diagram(seq_diagram)

    obj.create_and_persist_lifelines('l1')
    obj.create_and_persist_lifelines('l2')

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

    obj.create_and_persist_lifelines('l1')
    obj.create_and_persist_lifelines('l2')

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
