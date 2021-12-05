class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    
    def pre_order(self):
        output = []
        
        def _traverse(_root):
            output.append(_root.value)
            if _root.left is not None:
                _traverse(_root.left)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse
        # _traverse(self.root)
        # return output
    
    def find_max(self):
        # define a holder for _max
        _max = self.root.value
        # define a closure function
        def _traverse(node):
            nonlocal _max
            # compare current value with _max
            _max = node.value if node.value > _max else _max
            # if node.value > _max:
                # _max = node.value
            # recursively call closure function for left and right
            if node.left:
                _traverse(node.left)
            if node.right:
                _traverse(node.right)
        # call closure function for root
        _traverse(self.root)
        # return _max
        return _max


def create_tree():
    tree=Tree()
    tree.root=Node(5)
    tree.root.left=Node(8)
    tree.root.right=Node(12)
    tree.root.left.left=Node(-2)
    tree.root.left.right=Node(6)
    tree.root.right.left=Node(1)
    return tree

if __name__ == "__main__":
    tree = create_tree()
    traverse= tree.pre_order()
    print(traverse(tree.root))
    print(tree.find_max())
