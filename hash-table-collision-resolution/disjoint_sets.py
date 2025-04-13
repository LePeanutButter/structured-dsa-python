"""
This module implements two data structures:
1. DisjointSets – a simple disjoint set (union-find) implementation that manages 
   sets of elements and supports union operations.
2. HashTable – a hash table that uses sorted lists as buckets. In addition to basic 
   insertion, search, and deletion operations, it integrates DisjointSets to merge 
   bucket indices and associated values through union operations.

The module demonstrates these data structures with a sample dataset representing 
Colombian coffee exports.
"""

from sys import stdin
from random import randint
from time import time

class DisjointSets:
    """
    A simple implementation of a disjoint set (union-find) data structure.
    Each element is initially placed in its own singleton set. The union operation 
    merges two sets. This implementation uses Python's built-in set type without advanced 
    optimizations like path compression.
    """

    def __init__(self, A):
        """
        Initialize the disjoint sets structure using the iterable A.
        
        Args:
            A (iterable): An iterable of elements to be placed into individual sets.
        """
        self.sets = [set([x]) for x in A]

    def getSets(self):
        """
        Retrieve the current list of disjoint sets.
        
        Returns:
            list: A list of sets, each representing a connected component.
        """
        return self.sets

    def findSet(self, x):
        """
        Find and return the set that contains the element x.
        
        Args:
            x: The element to locate.
        
        Returns:
            set or None: The set containing x if found; otherwise, None.
        """
        for si in self.sets:
            if x in si:
                return si
        return None

    def makeSet(self, x):
        """
        Create a new singleton set containing the element x if it does not already exist.
        
        Args:
            x: The element to add.
        
        Returns:
            set: The new or existing set that contains the element x.
        """
        if self.findSet(x) is None:
            self.sets.append(set([x]))
            return self.sets[len(self.sets)-1]
        return self.findSet(x)

    def union(self, x, y):
        """
        Merge the sets that contain elements x and y. If either element is not yet present,
        a new singleton set is created for it. The two sets are then merged into one, removing 
        the old sets.
        
        Args:
            x: The first element.
            y: The second element.
        """
        s1 = self.findSet(x)
        s2 = self.findSet(y)

        if s1 is None:
            s1 = self.makeSet(x)
        if s2 is None:
            s2 = self.makeSet(y)
        if s1 != s2:
            s3 = s1.union(s2)
            self.sets.remove(s1)
            self.sets.remove(s2)
            self.sets.append(s3)

    def connectedComponents(self, Arcs):
        """
        Given a list of arcs (edge pairs), perform union on the endpoints of each arc.
        After processing, only components (sets) with more than one element are returned.
        The intermediate state of the sets is printed after processing each arc.
        
        Args:
            Arcs (list): A list of tuples where each tuple represents an edge (x, y).
        
        Returns:
            list: A list of sets, each containing at least two connected elements.
        """
        for e in Arcs:
            self.union(e[0], e[1])
            print('After processing arc', e, self.sets)
        result = []
        for si in self.sets:
            if len(si) > 1:
                result.append(si)
        return result


class HashTable:
    """
    A simple hash table that uses sorted lists as buckets for storing key-value tuples.
    In addition to performing standard hash table operations (insert, search, remove), 
    this class uses a DisjointSets instance to perform union operations between the bucket index 
    (derived from the key) and the inserted value.
    """

    def __init__(self, size):
        """
        Initialize the hash table with a fixed number of buckets.
        
        Args:
            size (int): The number of buckets to use in the hash table.
        """
        self.size = size
        self.elements = [ [] for _ in range(size)]
        self.disjoint_sets = DisjointSets([x for x in range(size)])

    def hash(self, key):
        """
        Compute the hash index for a given key.
        
        Args:
            key: The key to hash.
        
        Returns:
            int: The bucket index computed as hash(key) modulo the table size.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table. The pair is appended to the bucket 
        corresponding to the hashed key, and the bucket is then sorted. Following insertion, 
        a union operation is performed in the disjoint sets between the bucket index and the value.
        
        Args:
            key: The key under which the value is stored.
            value: The value to be stored.
        """
        index = self.hash(key)
        entry = (key, value)
        self.elements[index].append(entry)
        self.elements[index].sort()
        # Realiza una unión en los conjuntos disjuntos
        self.disjoint_sets.union(index, value)

    def search(self, key):
        """
        Search for the value associated with the provided key using binary search on 
        the sorted bucket.
        
        Args:
            key: The key to search for.
        
        Returns:
            The value associated with the key if found; otherwise, None.
        """
        index = self.hash(key)
        entry_list = self.elements[index]
        left, right = 0, len(entry_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if entry_list[mid][0] == key:
                return entry_list[mid][1]
            elif entry_list[mid][0] < key:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def remove(self, key):
        """
        Remove the key-value pair corresponding to the provided key from the hash table.
        
        Args:
            key: The key of the element to be removed.
        """
        index = self.hash(key)
        entry_list = self.elements[index]
        for i in range(len(entry_list)):
            if entry_list[i][0] == key:
                del entry_list[i]
                break

    def printElements(self):
        """
        Print the contents of each bucket in the hash table.
        """
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])


def main():
    """
    Demonstrate the use of the HashTable and DisjointSets classes using a sample dataset.
    
    The sample data represents export records (e.g., Colombian coffee exports). 
    Each record is a tuple where the key is a tuple containing export details (such as 
    country, date, and company name) and the value is a numerical export value.
    
    The function performs the following operations:
      - Inserting all records into the hash table.
      - Printing the entire hash table.
      - Searching for a specific record.
      - Measuring and printing the total execution time.
      - Printing the disjoint sets formed by the union operations.
    """
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
    t2 = time()
    print("Tiempo de ejecución:", t2 - t1, "segundos")
    print('Conjuntos disjuntos:', hashtable.disjoint_sets.getSets())

if __name__ == "__main__":
    main()