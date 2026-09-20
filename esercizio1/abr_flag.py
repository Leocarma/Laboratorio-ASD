class NodeFlag:
    # Rappresenta un nodo con un interruttore (flag) per gestire i duplicati
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.has_duplicate = False # Flag inizialmente spento

class ABRFlag:
    # ABR che accende un Flag booleano quando incontra un duplicato,
    # risparmiando la creazione di un nuovo nodo fisico.
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = NodeFlag(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # Se la chiave è uguale a una già esistente, accendiamo solo il flag
        if key == node.key:
            node.has_duplicate = True
        elif key < node.key:
            if node.left is None:
                node.left = NodeFlag(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = NodeFlag(key)
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
        # Conta quanti nodi fisici sono stati allocati, ignorando i flag accesi
        if node is None:
            return 0
        return 1 + self._conta_nodi_recursive(node.left) + self._conta_nodi_recursive(node.right)
