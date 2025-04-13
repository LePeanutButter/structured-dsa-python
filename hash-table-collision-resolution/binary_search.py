"""
Module that implements a simple hash table with separate chaining using sorted lists.
Each bucket is maintained as a sorted list of (key, value) tuples, allowing binary search
within a bucket for faster lookup. The module demonstrates a sample use case where export
data (for example, Colombian coffee exports) is inserted, printed, and searched.
"""

from sys import stdin
from random import randint
from time import time

class HashTable:
    """
    A hash table implementation that uses sorted lists (separate chaining) for collision resolution.
    
    Attributes:
        size (int): The number of buckets in the hash table.
        elements (list): A list of lists, where each inner list represents a bucket containing (key, value) tuples.
    """
    
    def __init__(self, size):
        """
        Initialize the HashTable with a specified number of buckets.
        
        Args:
            size (int): The desired number of buckets.
        """
        self.size = size
        self.elements = [ [] for _ in range(size)]

    def hash(self, key):
        """
        Compute the hash index for a given key.
        
        Args:
            key: The key to hash.
            
        Returns:
            int: The bucket index for the key within the range [0, size).
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        After insertion, the bucket is sorted based on the key.
        
        Args:
            key: The key to insert.
            value: The value associated with the key.
        """
        index = self.hash(key)
        entry = (key, value)
        self.elements[index].append(entry)
        self.elements[index].sort()

    def search(self, key):
        """
        Search for the value associated with a given key using binary search.
        
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
        Remove a key-value pair from the hash table.
        Searches for the key in the appropriate bucket and deletes the matching entry.
        
        Args:
            key: The key to remove from the hash table.
        """
        index = self.hash(key)
        entry_list = self.elements[index]
        for i in range(len(entry_list)):
            if entry_list[i][0] == key:
                del entry_list[i]
                break

    def printElements(self):
        """
        Print the current state of the hash table.
        For each bucket, the bucket index and its list of (key, value) entries are printed.
        """
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])


def main():
    """
    Demonstrate the use of the HashTable with sample data.
    
    The sample data represents export records (e.g., Colombian coffee exports) with each record
    being a tuple that contains an export detail tuple and its associated value.
    The function measures and prints the execution time of the insert and search operations.
    """

    new_data = [
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
    for e in new_data:
        hashtable.insert(e[0], e[1])
    hashtable.printElements()
    print('Searching for ', ('Francia', '11-06-2021', 'Café Parisien SAS'), ': ', hashtable.search(('Francia', '11-06-2021', 'Café Parisien SAS')))
    t2 = time()
    print("Tiempo de ejecución:", t2 - t1, "segundos")

if __name__ == "__main__":
    main()