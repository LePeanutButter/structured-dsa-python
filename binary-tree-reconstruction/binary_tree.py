from sys import stdin

class Nodo:
    """
    Represents a node in a binary tree.
    
    Attributes:
        valor (str): The value stored in this node.
        izquierda (Nodo): The left child node.
        derecha (Nodo): The right child node.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    """
    Provides methods to reconstruct a binary tree from pre-order and in-order traversals,
    and to perform a post-order traversal on the tree.
    """
    def __init__(self):
        self.raiz = None

    def construir_arbol(self, preorden, inorden):
        """
        Reconstructs the binary tree given its pre-order and in-order traversal strings.
        
        Args:
            preorden (str): A string representing the pre-order traversal.
            inorden (str): A string representing the in-order traversal.
        
        Returns:
            Nodo: The root node of the reconstructed binary tree.
        """
        if not preorden or not inorden:
            return None
        
        valor_raiz = preorden[0]
        nodo_raiz = Nodo(valor_raiz)
        indice_raiz_inorden = inorden.index(valor_raiz)
        
        preorden_izquierda = preorden[1:indice_raiz_inorden + 1]
        preorden_derecha = preorden[indice_raiz_inorden + 1:]
        inorden_izquierda = inorden[:indice_raiz_inorden]
        inorden_derecha = inorden[indice_raiz_inorden + 1:]
        
        nodo_raiz.izquierda = self.construir_arbol(preorden_izquierda, inorden_izquierda)
        nodo_raiz.derecha = self.construir_arbol(preorden_derecha, inorden_derecha)
        return nodo_raiz

    def posorden(self, nodo):
        """
        Performs a post-order traversal of the binary tree starting from the given node.
        
        Args:
            nodo (Nodo): The current node to process.
        
        Returns:
            str: A string representing the post-order traversal from this node.
        """
        if nodo is None:
            return ''
        return (self.posorden(nodo.izquierda) +
                self.posorden(nodo.derecha) +
                nodo.valor)

def main():
    """
    Reads pre-order and in-order traversal strings from standard input,
    reconstructs the binary tree, and prints its post-order traversal.
    """
    entrada = stdin.readline().strip().split()
    preorden = entrada[0]
    inorden = entrada[1]
    
    arbol = ArbolBinario()
    raiz = arbol.construir_arbol(preorden, inorden)
    posorden_resultante = arbol.posorden(raiz)
    print(posorden_resultante)

if __name__ == "__main__":
    main()