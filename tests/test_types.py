import random
import pytest

from circkit.arithmetic import ArithmeticCircuit

def test_random():
    C = ArithmeticCircuit(name="TwoRandoms")

    # note: add_node is not needed to be called usually
    op5 = C.CONST(5)
    with pytest.raises(TypeError):
        C.add_node(op5)
    with pytest.raises(TypeError):
        C.add_output(op5)

    # correct usage (create node)
    C.add_output(op5())

    op_rand = C.RND()
    with pytest.raises(TypeError):
        C.add_node(op_rand)
    with pytest.raises(TypeError):
        C.add_output(op_rand)

    # correct usage (create node)
    C.add_output(op_rand())
