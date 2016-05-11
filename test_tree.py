from unittest import TestCase
from tree import Tree


class TestTree(TestCase):
    def test__add(self):
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
        self.assertIs(verify(tree.get_root()), True, "Tree is not proper BST")


def max_num(node):
    if not node:
        return float("-inf")
    left = max_num(node.left)
    right = max_num(node.right)
    return max(node.data, left, right)


def min_num(node):
    if not node:
        return float("inf")
    left = min_num(node.left)
    right = min_num(node.right)
    return min(node.data, left, right)


def verify(node):
    if not node:
        return True
    if (max_num(node.left) <= node.data <= min_num(node.right) and
            verify(node.left) and verify(node.right)):
        return True
    else:
        return False
