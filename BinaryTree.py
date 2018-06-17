class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            self._find(val, node.l)
        elif val > node.v and node.r is not None:
            self._find(val, node.r)

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.l)
            print(str(node.v) + ' ')
            self._print_tree(node.r)

    def get_height(self):
        return 0 if self.root is None else self._get_height(self.root)

    def _get_height(self, node):
        left_height = 0 if node.l is None else self._get_height(node.l)
        right_height = 0 if node.r is None else self._get_height(node.r)
        return max(left_height, right_height) + 1
