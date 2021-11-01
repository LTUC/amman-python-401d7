from recursion import __version__
from recursion.factorial import fact

def test_version():
    assert __version__ == '0.1.0'

def test_fact_5():
    expected=120
    actual=fact(5)
    assert actual == expected

def test_fact_1():
    expected=1
    actual=fact(1)
    assert actual == expected

