from fizz_buzz import __version__
from fizz_buzz.fizz_buzz import is_fizz_buzz

def test_version():
    assert __version__ == '0.1.0'


def test_fizz_25():
    expected='buzz'
    actual=is_fizz_buzz(25)
    assert expected == actual


def test_fizz_3():
    assert 'fizz' == is_fizz_buzz(3)


def test_fizz_15():
    expected='fizz buzz'
    actual=is_fizz_buzz(15)
    assert expected == actual

