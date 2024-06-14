import random
import pytest

from circkit.arithmetic import ArithmeticCircuit
from circkit.arithmetic import OptArithmeticCircuit


class IntegerRing:
    def __init__(self):
        self.counter = 999

    def random_element(self):
        self.counter += 1
        return self.counter

    def __call__(self, value):
        return int(value)


def test_random():
    C = ArithmeticCircuit(base_ring=IntegerRing(), name="TwoRandoms")
    a = C.RND()()
    b = C.RND()()
    C.add_output(a)
    C.add_output(b)
    out = C.evaluate([])
    assert out == [1000, 1001]

    C = OptArithmeticCircuit(base_ring=IntegerRing(), name="TwoRandomsOpt")
    a = C.RND()()
    b = C.RND()()
    C.add_output(a)
    C.add_output(b)
    out = C.evaluate([])
    assert out == [1000, 1001]
