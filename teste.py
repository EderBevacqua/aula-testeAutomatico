from main import soma, mult
import pytest


def test_soma():
    assert soma(2,4)==6

def test_mult():
    assert mult(2,4)==8