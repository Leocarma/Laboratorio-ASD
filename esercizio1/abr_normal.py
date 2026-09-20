class NodeNormal:
    # Rappresenta un singolo nodo dell'Albero Binario di Ricerca (ABR)
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class ABRNormal:
    # Albero Binario di Ricerca classico
    # I duplicati vengono inseriti fisicamente come nuovi nodi figli.
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = NodeNormal(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # Se la chiave è minore o uguale, va a sinistra (creando un nuovo nodo per il duplicato)
        if key <= node.key:
            if node.left is None:
                node.left = NodeNormal(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = NodeNormal(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        # Ritorna False se arriva in fondo senza trovare nulla
        if node is None:
            return False
        # Ritorna True appena trova il nodo con la chiave cercata
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def altezza(self):
        return self._altezza_recursive(self.root)

    def _altezza_recursive(self, node):
        # L'altezza di un albero vuoto è -1
        if node is None:
            return -1
        left_h = self._altezza_recursive(node.left)
        right_h = self._altezza_recursive(node.right)
        return max(left_h, right_h) + 1

    def conta_nodi(self):
        return self._conta_nodi_recursive(self.root)

    def _conta_nodi_recursive(self, node):
        # Conta quanti nodi fisici sono stati allocati in memoria
        if node is None:
            return 0
        return 1 + self._conta_nodi_recursive(node.left) + self._conta_nodi_recursive(node.right)
