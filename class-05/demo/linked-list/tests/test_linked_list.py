from linked_list import __version__
from linked_list.linked_list import LinkedList, Node

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


def test_append_3_values(ll):
    expected = 'head -> 5 -> Hello -> 1.67 -> None'
    actual = ll.__str__()
    assert expected == actual


def test_append_to_existing_ll(ll):
    ll.append(True)
    expected = 'head -> 5 -> Hello -> 1.67 -> True -> None'
    actual = ll.__str__()
    assert expected == actual



@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append('Hello')
    ll.append(1.67)
    return ll