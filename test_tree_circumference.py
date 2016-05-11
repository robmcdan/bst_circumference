from unittest import TestCase
from tree_circumference import *
import collections
from tree import *

class TestTreeCircumference(TestCase):
    def are_equal(self, x, y):
        return collections.Counter(x) == collections.Counter(y)

    def test_get_circumference(self):
        tree = self.make_test_tree()
        result = get_circumference(tree.get_root())
        self.assertTrue(collections.Counter([50, 25, 12, 31, 42, 56, 68, 87, 75]) ==
                        collections.Counter(result), "circumference did not match expected value")

    def test_get_circumference_empty(self):
        tree = Tree()
        result = get_circumference(tree.get_root())
        self.assertTrue(collections.Counter([]) ==
                        collections.Counter(result), "circumference did not match expected value")

    def test_get_circumference_only_leftchild(self):
        tree = Tree()
        tree.add(50)
        tree.add(25)
        result = get_circumference(tree.get_root())
        self.assertTrue(collections.Counter([50, 25]) ==
                        collections.Counter(result), "circumference did not match expected value")

    def test_get_circumference_only_rightchild(self):
        tree = Tree()
        tree.add(50)
        tree.add(75)
        result = get_circumference(tree.get_root())
        self.assertTrue(collections.Counter([50, 75]) ==
                        collections.Counter(result), "circumference did not match expected value")

    def test_get_circumference_linked_list_right(self):
        tree = Tree()
        tree.add(50)
        tree.add(75)
        tree.add(100)
        result = get_circumference(tree.get_root())
        self.assertTrue(collections.Counter([50, 100, 75]) ==
                        collections.Counter(result), "circumference did not match expected value")

    def test_get_circumference_linked_list_left(self):
        tree = Tree()
        tree.add(50)
        tree.add(25)
        tree.add(12)
        result = get_circumference(tree.get_root())
        self.assertTrue(collections.Counter([50, 25, 12]) ==
                        collections.Counter(result), "circumference did not match expected value")

    def make_test_tree(self):
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
        return tree
