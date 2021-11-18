from trees import __version__
import trees
from trees.tree import Tree, Node
import pytest


def test_version():
    assert __version__ == '0.1.0'


#     A
#  B     C
# D E    f
def test_pre_order(create_tree):

    excepted = ["A", "B", "D", "E", "C", "F"]
    assert create_tree.pre_order(create_tree.root) == excepted

@pytest.fixture
def create_tree():
    tree=Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree


