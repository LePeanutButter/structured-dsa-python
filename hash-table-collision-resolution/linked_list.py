"""
Module that implements a simple hash table with separate chaining using linked lists.
It demonstrates the usage of these data structures with a sample dataset representing
Colombian coffee exports to various countries.
"""

from sys import stdin
from random import randint
from time import time

class Node:
    """
    A node in a singly linked list representing a key-value pair.
    
    Attributes:
        key: The key associated with the node.
        value: The value associated with the node.
        next: Pointer to the next node in the list (initially None).
    """

    def __init__(self, key, value):
        """
        Initialize a new Node instance.
        
        Args:
            key: The key for the node.
            value: The value for the node.
        """
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    """
    A singly linked list used to store nodes containing key-value pairs.
    
    Attributes:
        head: The first node in the linked list (None if the list is empty).
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def insert(self, key, value):
        """
        Insert a new node with the given key and value at the end of the list.
        
        Args:
            key: The key of the new node.
            value: The value of the new node.
        """
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        """
        Search for a node by its key in the linked list.
        
        Args:
            key: The key to search for.
        
        Returns:
            The value associated with the key if found; otherwise, None.
        """
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        """
        Remove the node with the specified key from the linked list.
        
        Args:
            key: The key of the node to remove.
        """
        if not self.head:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

class HashTable:
    """
    A hash table implementation that uses separate chaining (with linked lists)
    to resolve hash collisions.
    
    Attributes:
        size: The number of buckets available in the hash table.
        elements: A list of LinkedList instances representing the buckets.
    """

    def __init__(self, size):
        """
        Initialize the hash table with a given number of buckets.
        
        Args:
            size: The size (number of buckets) for the hash table.
        """
        self.size = size
        self.elements = [LinkedList() for _ in range(size)]

    def hash(self, key):
        """
        Compute the hash index for a given key.
        
        Args:
            key: The key to be hashed.
        
        Returns:
            The index in the range [0, size) for the given key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key: The key for insertion.
            value: The value corresponding to the key.
        """
        index = self.hash(key)
        self.elements[index].insert(key, value)

    def search(self, key):
        """
        Search for a value by its corresponding key in the hash table.
        
        Args:
            key: The key associated with the desired value.
        
        Returns:
            The value associated with the key if found; otherwise, None.
        """
        index = self.hash(key)
        return self.elements[index].search(key)

    def remove(self, key):
        """
        Remove a key-value pair from the hash table by its key.
        
        Args:
            key: The key for the key-value pair to remove.
        """
        index = self.hash(key)
        self.elements[index].remove(key)

    def printElements(self):
        """
        Print the contents of the hash table.
        For each bucket, the index and all its nodes (key, value pairs) are printed.
        """
        for index in range(len(self.elements)):
            print(index, ': ', end='')
            current = self.elements[index].head
            while current:
                print('(', current.key, ',', current.value, ')', end=' -> ')
                current = current.next
            print('None')

def main():
    """
    Main function that demonstrates the usage of the hash table.
    A sample export dataset (Colombian coffee exports) is constructed,
    and each record is inserted into the hash table. The elements are then printed,
    and a sample search is performed. Execution time is measured.
    """
    
    # Datos de ejemplo para representar la exportación de café desde Colombia hacia otros países
    export_data = [
        (('Francia', '11-06-2021', 'Café Colombiano SAS'), 4500),
        (('Italia', '10-06-2021', 'Gustos Italianos SRL'), 5000),
        (('Estados Unidos', '09-06-2021', 'Java & Co.'), 5200),
        (('Alemania', '08-06-2021', 'Kaffee GmbH'), 4800),
        (('Reino Unido', '07-06-2021', 'British Beans Ltd.'), 4900),
        (('Japón', '06-06-2021', 'Tokyo Roasters Inc.'), 5100),
        (('Canadá', '05-06-2021', 'Maple Beans Co.'), 4700),
        (('Australia', '04-06-2021', 'Aussie Breweries Pty Ltd.'), 5300),
        (('Brasil', '03-06-2021', 'Café Brasileiro SA'), 4600),
        (('España', '02-06-2021', 'Café Español SL'), 5400)
    ]

    t1 = time()
    hashtable = HashTable(13)
    for e in export_data:
        hashtable.insert(e[0], e[1])
    hashtable.printElements()
    t2 = time()
    print('Searching for ', ('Francia', '11-06-2021', 'Café Colombiano SAS'), ': ',
          hashtable.search(('Francia', '11-06-2021', 'Café Colombiano SAS')))
    print(f"El tiempo de ejecución fue: {t2 - t1}s")

if __name__ == "__main__":
    main()