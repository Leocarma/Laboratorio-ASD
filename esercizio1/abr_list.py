class NodeList:
    def __init__(self, key):
        self.key = key
        # List of elements with the same key
        self.duplicates = [key]
        self.left = None
        self.right = None

class ABRList:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = NodeList(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key == node.key:
            node.duplicates.append(key)
        elif key < node.key:
            if node.left is None:
                node.left = NodeList(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = NodeList(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def altezza(self):
        return self._altezza_recursive(self.root)

    def _altezza_recursive(self, node):
        if node is None:
            return -1
        left_h = self._altezza_recursive(node.left)
        right_h = self._altezza_recursive(node.right)
        return max(left_h, right_h) + 1

    def conta_nodi(self):
        return self._conta_nodi_recursive(self.root)

    def _conta_nodi_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._conta_nodi_recursive(node.left) + self._conta_nodi_recursive(node.right)
