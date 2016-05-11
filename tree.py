class Node:
    """
    node of a binary tree
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left != None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(data, node.right)

if __name__ == '__main__':
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
