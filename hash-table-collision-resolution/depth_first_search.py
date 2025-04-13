"""
Module that implements a hash table using dictionaries as adjacency lists with 
basic CRUD operations and a depth-first search (DFS) demonstration. The module 
illustrates these operations using a sample dataset representing Colombian coffee 
exports to various countries.
"""

from sys import stdin
from random import randint
from time import time

# Color constants (not actively used in this module, but may be reserved for future use)
WHITE = "white"
BLACK = "black"
GRAY = "gray"
import math

class HashTable:
    """
    A hash table implementation that uses a list of dictionaries to simulate 
    adjacency lists. Each dictionary represents a bucket where each key is 
    associated with its corresponding value.
    """
    
    def __init__(self, size):
        """
        Initialize the hash table with a specified number of buckets.
        
        Args:
            size (int): The number of buckets for the hash table.
        """
        self.elements = [{} for x in range(size)]  # Usamos diccionarios para listas de adyacencias

    def getElements(self):
        """
        Retrieve the list of bucket dictionaries.
        
        Returns:
            list: The list of dictionaries representing hash table buckets.
        """
        return self.elements

    def printElements(self):
        """
        Print the content of each bucket in the hash table.
        """
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])

    def hash(self, key):
        """
        Compute the hash index for a provided key.
        
        Args:
            key: The key to hash.
        
        Returns:
            int: The index computed as hash(key) modulo the number of buckets.
        """
        return hash(key) % len(self.elements)

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table. The appropriate bucket is 
        determined by hashing the key. A message is printed indicating where the 
        insertion occurs.
        
        Args:
            key: The key under which the value will be stored.
            value: The value to store.
        """
        index = self.hash(key)
        print('Inserting', value, 'with key', key, 'on index', index)
        # Insertamos en la lista de adyacencia correspondiente al índice
        self.elements[index][key] = value

    def search(self, key):
        """
        Search for the value associated with the given key.
        
        Args:
            key: The key to search for.
        
        Returns:
            The value associated with the key if found; otherwise, None.
        """
        index = self.hash(key)
        # Buscamos en la lista de adyacencia correspondiente al índice
        return self.elements[index].get(key, None)

    def update(self, key, value):
        """
        Update the value for an existing key in the hash table. If the key exists 
        in the appropriate bucket, its value is updated.
        
        Args:
            key: The key whose value should be updated.
            value: The new value to assign to the key.
        """
        index = self.hash(key)
        # Actualizamos el valor en la lista de adyacencia correspondiente al índice
        if key in self.elements[index]:
            self.elements[index][key] = value

    def delete(self, key):
        """
        Delete the key-value pair from the hash table. The key is located by its 
        hash index and removed if it exists.
        
        Args:
            key: The key to delete.
        """
        index = self.hash(key)
        # Eliminamos el valor en la lista de adyacencia correspondiente al índice
        if key in self.elements[index]:
            del self.elements[index][key]

    def dfs(self, index):
        """
        Perform a depth-first search (DFS) on the bucket (adjacency list) at the 
        specified index. In this implementation, each key in the bucket's dictionary 
        is treated as a vertex. The DFS visits and prints every vertex and its value.
        
        Args:
            index (int): The index of the bucket on which to perform DFS.
        """
        def _dfs_visit(graph, vertex, visited):
            visited[vertex] = True
            print(f"Visited {vertex}: {graph[vertex]}")
            for neighbor in graph:  # Solo se debe iterar sobre las claves del mismo diccionario
                if neighbor not in visited:
                    _dfs_visit(graph, neighbor, visited)

        # Obtenemos la lista de adyacencia del índice especificado
        graph = self.elements[index]
        visited = {}
        for vertex in graph:
            if vertex not in visited:
                _dfs_visit(graph, vertex, visited)

def main():
    """
    Demonstrate the usage of the HashTable by performing insertion, search, update, 
    deletion, and DFS operations using a sample dataset.
    
    The sample data consists of tuples where each key is a tuple representing export 
    details (e.g., country, date, company name) and the value is an associated numeric value.
    Execution time is measured for the overall operations.
    """

    # Datos ficticios para representar la exportación de café desde Colombia a otros países
    export_data = [
        (('Francia', '11-06-2021', 'Café Parisien SAS'), 4500),
        (('Italia', '12-06-2021', 'Gusti Italiani SRL'), 5000),
        (('Estados Unidos', '13-06-2021', 'Java & Co.'), 5200),
        (('Alemania', '14-06-2021', 'Kaffee GmbH'), 4800),
        (('Reino Unido', '15-06-2021', 'British Beans Ltd.'), 4900),
        (('Japón', '16-06-2021', 'Tokyo Roasters Inc.'), 5100),
        (('Canadá', '17-06-2021', 'Maple Beans Co.'), 4700),
        (('Australia', '18-06-2021', 'Aussie Breweries Pty Ltd.'), 5300),
        (('Brasil', '19-06-2021', 'Café Brasileiro SA'), 4600),
        (('España', '20-06-2021', 'Café Español SL'), 5400)
    ]

    t1 = time()
    hashtable = HashTable(13)
    for e in export_data:
        hashtable.insert(e[0], e[1])
    hashtable.printElements()
    print('Searching for ', ('Francia', '11-06-2021', 'Café Parisien SAS'), ': ', hashtable.search(('Francia', '11-06-2021', 'Café Parisien SAS')))
    print('Searching for ', ('Italia', '12-06-2021', 'Gusti Italiani SRL'), ': ', hashtable.search(('Italia', '12-06-2021', 'Gusti Italiani SRL')))
    print('Searching for ', ('Japón', '16-06-2021', 'Tokyo Roasters Inc.'), ': ', hashtable.search(('Japón', '16-06-2021', 'Tokyo Roasters Inc.')))
    hashtable.update(('Reino Unido', '15-06-2021', 'British Beans Ltd.'), 4950)
    print('Updated Search for ', ('Reino Unido', '15-06-2021', 'British Beans Ltd.'), ': ', hashtable.search(('Reino Unido', '15-06-2021', 'British Beans Ltd.')))
    hashtable.delete(('Brasil', '19-06-2021', 'Café Brasileiro SA'))
    print('Post-delete Search for ', ('Brasil', '19-06-2021', 'Café Brasileiro SA'), ': ', hashtable.search(('Brasil', '19-06-2021', 'Café Brasileiro SA')))

    # Realizamos DFS en los índices correspondientes
    print("DFS on index 0:")
    hashtable.dfs(0)
    print("DFS on index 7:")
    hashtable.dfs(7)

    t2 = time()
    print("El tiempo de ejecución fue", t2 - t1, "s")

if __name__ == "__main__":
    main()