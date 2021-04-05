from activity.activity_diagram import ActivityDiagram
from activity.decision_node import DecisionStream


def test_activity_diagram():
    obj = ActivityDiagram('ad1')
    assert 'ad1' == obj.name


def test_activity_diagram2():
    obj = ActivityDiagram('ad2')
    assert 'ad2' == obj.name


def test_activity_diagram3():
    obj = ActivityDiagram('ad3')
    assert 'ad3' == obj.name


def test_create_initial_node():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    assert 'n1' == obj.elements.start_node


def test_create_initial_node2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    assert 'n2' == obj.elements.start_node


def test_create_initial_node3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    assert 'n3' == obj.elements.start_node


def test_create_activity():
    obj = ActivityDiagram('ad1')

    obj.create_initial_node('n1')
    obj.elements.create_activity('at1')

    assert 'at1' == obj.elements.activity_name[0]
    assert 0 == obj.elements.elements_order[0]


def test_create_activity2():
    obj = ActivityDiagram('ad2')

    obj.create_initial_node('n2')
    obj.elements.create_activity('at2')

    assert 'at2' == obj.elements.activity_name[0]
    assert 0 == obj.elements.elements_order[0]


def test_create_activity3():
    obj = ActivityDiagram('ad3')

    obj.create_initial_node('n3')

    obj.elements.create_activity('at3')
    obj.elements.create_activity('at3.1')

    assert 'at3' == obj.elements.activity_name[0]
    assert 0 == obj.elements.elements_order[0]

    assert 'at3.1' == obj.elements.activity_name[1]
    assert 0 == obj.elements.elements_order[1]


def test_initiate_decision():
    obj = ActivityDiagram('ad1')

    obj.create_initial_node('n1')
    obj.elements.initiate_decision(1)

    assert [[]] == obj.elements.decision_node


def test_initiate_decision2():
    obj = ActivityDiagram('ad2')

    obj.create_initial_node('n2')
    obj.elements.initiate_decision(2)

    assert [[], []] == obj.elements.decision_node


def test_initiate_decision3():
    obj = ActivityDiagram('ad3')

    obj.create_initial_node('n3')
    obj.elements.initiate_decision(3)

    assert [[], [], []] == obj.elements.decision_node


def test_decision_create_activity():
    decision = DecisionStream()

    decision.create_activity("nda1")

    assert decision.elements[0] == 0
    assert decision.activity_node[0] == "nda1"


def test_decision_create_activity2():
    decision = DecisionStream()

    decision.create_activity("nda2")

    assert decision.elements[0] == 0
    assert decision.activity_node[0] == "nda2"


def test_decision_create_activity3():
    decision = DecisionStream()

    decision.create_activity("nda3")
    decision.create_activity("nda3.1")

    assert decision.elements[0] == 0
    assert decision.activity_node[0] == "nda3"

    assert decision.elements[1] == 0
    assert decision.activity_node[1] == "nda3.1"


def test_decision_create_transition():
    decision = DecisionStream()

    decision.create_transition("ndt1", 19.49)

    assert decision.transitions[0].transition_name == "ndt1"
    assert decision.transitions[0].transition_prob == 19.49


def test_decision_create_transition2():
    decision = DecisionStream()

    decision.create_transition("ndt2", 19.50)

    assert decision.transitions[0].transition_name == "ndt2"
    assert decision.transitions[0].transition_prob == 19.50


def test_decision_create_transition3():
    decision = DecisionStream()

    decision.create_transition("ndt3", 19.51)
    decision.create_transition("ndt3.1", 19.52)

    assert decision.transitions[0].transition_name == "ndt3"
    assert decision.transitions[0].transition_prob == 19.51

    assert decision.transitions[1].transition_name == "ndt3.1"
    assert decision.transitions[1].transition_prob == 19.52


def test_decision_create_merge():
    decision = DecisionStream()

    decision.create_merge("ndm1")

    assert decision.elements[0] == 1
    assert decision.merge_node == "ndm1"


def test_decision_create_merge2():
    decision = DecisionStream()

    decision.create_merge("ndm2")

    assert decision.elements[0] == 1
    assert decision.merge_node == "ndm2"


def test_decision_create_merge3():
    decision = DecisionStream()

    decision.create_merge("ndm3")

    assert decision.elements[0] == 1
    assert decision.merge_node == "ndm3"


def test_create_decision():
    obj = ActivityDiagram('ad1')
    obj.create_initial_node('n1')
    obj.elements.initiate_decision(1)

    decision = DecisionStream()
    decision.create_activity('nda1')
    decision.create_transition('ndt1', 8.59)
    decision.create_merge('ndm1')

    obj.elements.create_decision(decision)

    assert obj.elements.decision_node[0][0].elements[0] == 0
    assert obj.elements.decision_node[0][0].activity_node[0] == 'nda1'

    assert (
        obj.elements.decision_node[0][0].transitions[0].transition_name
    ) == 'ndt1'

    assert (
        obj.elements.decision_node[0][0].transitions[0].transition_prob
    ) == 8.59

    assert obj.elements.decision_node[0][0].elements[1] == 1
    assert obj.elements.decision_node[0][0].merge_node == 'ndm1'


def test_create_decision2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')
    obj.elements.initiate_decision(1)

    decision = DecisionStream()
    decision.create_activity('nda2')
    decision.create_transition('ndt2', 9.50)
    decision.create_merge('nm1')

    obj.elements.create_decision(decision)

    assert obj.elements.decision_node[0][0].elements[0] == 0
    assert obj.elements.decision_node[0][0].activity_node[0] == 'nda2'

    assert (
        obj.elements.decision_node[0][0].transitions[0].transition_name
    ) == 'ndt2'

    assert (
        obj.elements.decision_node[0][0].transitions[0].transition_prob
    ) == 9.50

    assert obj.elements.decision_node[0][0].elements[1] == 1
    assert obj.elements.decision_node[0][0].merge_node == 'nm1'


def test_create_decision3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')
    obj.elements.initiate_decision(2)

    decision = DecisionStream()
    decision.create_activity('nda3.1')
    decision.create_transition('ndt3.1', 9.49)
    decision.create_merge('ndm3.1')

    obj.elements.create_decision(decision)

    decision = DecisionStream()
    decision.create_merge('ndm3.2')

    obj.elements.create_decision(decision)

    assert obj.elements.decision_node[0][0].elements[0] == 0
    assert obj.elements.decision_node[0][0].activity_node[0] == 'nda3.1'

    assert (
        obj.elements.decision_node[0][0].transitions[0].transition_name
    ) == 'ndt3.1'

    assert (
        obj.elements.decision_node[0][0].transitions[0].transition_prob
    ) == 9.49

    assert obj.elements.decision_node[0][0].elements[1] == 1
    assert obj.elements.decision_node[0][0].merge_node == 'ndm3.1'

    assert obj.elements.decision_node[0][1].elements[0] == 1
    assert obj.elements.decision_node[0][1].merge_node == 'ndm3.2'


def test_aux_decision():
    obj = ActivityDiagram('ad1')

    obj.create_initial_node('n1')
    obj.elements.aux_decision()

    assert obj.elements.elements_order[0] == 1
    assert obj.elements.decision_node_number == 1


def test_aux_decision2():
    obj = ActivityDiagram('ad2')
    obj.create_initial_node('n2')

    obj.elements.aux_decision()
    obj.elements.aux_decision()

    assert obj.elements.elements_order[1] == 1
    assert obj.elements.decision_node_number == 2


def test_aux_decision3():
    obj = ActivityDiagram('ad3')
    obj.create_initial_node('n3')

    obj.elements.aux_decision()
    obj.elements.aux_decision()
    obj.elements.aux_decision()

    assert obj.elements.elements_order[2] == 1
    assert obj.elements.decision_node_number == 3


def test_create_merge():
    obj = ActivityDiagram('ad1')

    obj.create_initial_node('n1')
    obj.elements.create_merge('m1')

    assert 'm1' == obj.elements.merge_node[0]
    assert 2 == obj.elements.elements_order[0]


def test_create_merge2():
    obj = ActivityDiagram('ad2')

    obj.create_initial_node('n2')
    obj.elements.create_merge('m2')

    assert 'm2' == obj.elements.merge_node[0]
    assert 2 == obj.elements.elements_order[0]


def test_create_merge3():
    obj = ActivityDiagram('ad3')

    obj.create_initial_node('n3')

    obj.elements.create_merge('m3')
    obj.elements.create_merge('m3.1')

    assert 'm3' == obj.elements.merge_node[0]
    assert 2 == obj.elements.elements_order[0]

    assert 'm3.1' == obj.elements.merge_node[1]
    assert 2 == obj.elements.elements_order[1]


def test_create_final():
    obj = ActivityDiagram('ad1')

    obj.create_initial_node('n1')
    obj.elements.create_final('f1')

    assert 'f1' == obj.elements.final_node
    assert 3 == obj.elements.elements_order[0]


def test_create_final2():
    obj = ActivityDiagram('ad2')

    obj.create_initial_node('n2')
    obj.elements.create_final('f2')

    assert 'f2' == obj.elements.final_node
    assert 3 == obj.elements.elements_order[0]


def test_create_final3():
    obj = ActivityDiagram('ad3')

    obj.create_initial_node('n3')

    obj.elements.create_final('f3')

    assert 'f3' == obj.elements.final_node
    assert 3 == obj.elements.elements_order[0]


def test_create_transition():
    obj = ActivityDiagram('ad1')

    obj.create_initial_node('n1')
    obj.create_transitions('t1', 0.01)

    assert 't1' == obj.transitions[0].transition_name
    assert 0.01 == obj.transitions[0].transition_prob


def test_create_transition2():
    obj = ActivityDiagram('ad2')

    obj.create_initial_node('n2')
    obj.create_transitions('t2', 0.09)

    assert 't2' == obj.transitions[0].transition_name
    assert 0.09 == obj.transitions[0].transition_prob


def test_create_transition3():
    obj = ActivityDiagram('ad3')

    obj.create_initial_node('n3')

    obj.create_transitions('t3', 0.90)
    obj.create_transitions('t3.1', 11.44)

    assert 't3' == obj.transitions[0].transition_name
    assert 0.90 == obj.transitions[0].transition_prob

    assert 't3.1' == obj.transitions[1].transition_name
    assert 11.44 == obj.transitions[1].transition_prob
