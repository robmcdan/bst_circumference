"""
print circumference of a binary tree (counter-clockwise)
"""
from state import State
from tree import *


def __is_leaf(node):
    return node.left is None and node.right is None


def __print_edges(node, state, should_print=True):
    nodes = []
    if node:
        # to ensure order, print node first when in left state
        if state.LEFT and (should_print or __is_leaf(node)):
           nodes.append(node.data)

        nodes.extend(__print_edges(node.left, state, should_print=(True if state.LEFT else False)))
        nodes.extend(__print_edges(node.right, state, should_print=(False if state.LEFT else True)))

        # to ensure order, print node last when in right state
        if state.RIGHT and (should_print or __is_leaf(node)):
             nodes.append(node.data)

    return nodes


def get_circumference(root):
    """
    prints the circumference of a binary tree in counter-clockwise order
    :param root: root node of the Tree
    :returns list of nodes in circumference, in counter-clockwise order
    """
    nodes = []
    if root:
        nodes.append(root.data)
        nodes.extend(__print_edges(root.left, State(True, False), True))
        nodes.extend(__print_edges(root.right, State(False, True), True))
    return nodes


if __name__ == '__main__':
    # test
    tree = Tree()
    tree.add(50)
    tree.add(25)
    tree.add(75)
    tree.add(12)
    tree.add(37)
    tree.add(31)
    tree.add(42)
    tree.add(62)
    tree.add(56)
    tree.add(68)
    tree.add(87)

    print get_circumference(tree.get_root())
