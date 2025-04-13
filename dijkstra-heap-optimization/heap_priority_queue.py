import math
import uuid
from random import randint


class Heap:
    """
    Implements a binary heap data structure that can function as either a max-heap
    or a min-heap based on its configuration.

    Attributes:
        data (list): The list that stores heap elements.
        config (bool): The heap type configuration; True for max-heap, False for min-heap.
    """

    def __init__(self, data=[], config=True):
        """
        Initialize a new Heap instance.

        Args:
            data (list, optional): An optional list of initial elements.
            config (bool, optional): If True, the heap is a max-heap; if False, a min-heap.
        """
        self.data = []
        self.config = config
        self.build(data[:])

    def left(self, index):
        """
        Calculate the index of the left child of the given node.

        Args:
            index (int): The index of the current node.
        
        Returns:
            int: The index of the left child.
        """
        return 2 * index + 1

    def right(self, index):
        """
        Calculate the index of the right child of the given node.

        Args:
            index (int): The index of the current node.
        
        Returns:
            int: The index of the right child.
        """
        return 2 * (index + 1)

    def parent(self, index):
        """
        Calculate the index of the parent of the given node.

        Args:
            index (int): The index of the current node.
        
        Returns:
            int: The index of the parent node.
        """
        return (index - 1) // 2

    def height(self):
        """
        Calculate the height of the heap based on the number of elements.
        Note: The height is computed as the ceiling of the log base 2 of the size.

        Returns:
            int: The height of the heap.
        """
        return math.ceil(math.log(len(self.data), 2))

    def __len__(self):
        """
        Return the number of elements in the heap.

        Returns:
            int: The size of the heap.
        """
        return len(self.data)

    def insert(self, new):
        """
        Insert a new element into the heap. After inserting, the heap is rebuilt
        to ensure the heap property is maintained.

        Args:
            new: The new element to insert.
        """
        self.data.append(new)
        self.build()

    def update(self, old, new):
        """
        Update an existing element in the heap by replacing it with a new value.
        The operation is implemented by deleting the old value and inserting the new value.

        Args:
            old: The element to be replaced.
            new: The new element to insert.
        """
        self.delete(old)
        self.insert(new)

    def delete(self, to_delete):
        """
        Delete an element from the heap. If the element is not found or the heap is empty,
        an exception is raised. After deletion, the heap is rebuilt.

        Args:
            to_delete: The element to delete from the heap.
        
        Raises:
            Exception: If the heap is empty or the element is not present in the heap.
        """
        if len(self) == 0:
            raise Exception("El montón está vacio")
        if to_delete not in self.data:
            raise Exception("El elemento no está en el montón")
        self.data.remove(to_delete)
        self.build()

    def build(self, data=[]):
        """
        Build (or rebuild) the heap from the provided data. If a new non-empty list
        is given, the heap's data is replaced by it.

        Args:
            data (list, optional): A new list of elements to build the heap from.
        """
        if data and len(data) > 0 and isinstance(data, list):
            self.data = data
        for index in range(len(self) // 2, -1, -1):
            self.heapify(index)

    def heapify(self, index):
        """
        Heapify the tree rooted at the given index according to the heap configuration.
        For a max-heap, it calls max_heapify; for a min-heap, it calls min_heapify.

        Args:
            index (int): The index of the root of the subtree to heapify.
        """
        if self.config:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def max_heapify(self, index):
        """
        Maintain the max-heap property for the subtree rooted at the given index.
        This ensures that each parent is greater than or equal to its child nodes.

        Args:
            index (int): The index of the current node.
        """
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

    def peek(self):
        """
        Return the element at the root of the heap (the highest priority element).

        Returns:
            The top element in the heap.
        """
        return self.data[0]

    def min_heapify(self, index):
        """
        Placeholder for min-heapify function. Not implemented in this version.
        """
        return

    def __str__(self):
        """
        Return a string representation of the heap.

        Returns:
            str: The string representation of the heap's internal array.
        """
        return str(self.data)


class PriorityQueue:
    """
    Implements a priority queue using the Heap class. This queue supports both enqueue
    and dequeue operations based on the heap configuration.
    """

    def __init__(self, data=[], config=True):
        """
        Initialize a new PriorityQueue instance.

        Args:
            data (list, optional): A list of initial elements.
            config (bool, optional): Heap configuration; True for a max-heap priority queue,
                False for a min-heap.
        """
        self.data = Heap(data, config)

    def __str__(self):
        """
        Return a string representation of the priority queue.

        Returns:
            str: The string representation of the underlying heap.
        """
        return str(self.data)

    def __len__(self):
        """
        Return the number of elements in the priority queue.

        Returns:
            int: The size of the priority queue.
        """
        return len(self.data)

    def enqueue(self, new):
        """
        Add a new element to the priority queue.

        Args:
            new: The new element to add.
        """
        self.data.insert(new)

    def dequeue(self):
        """
        Remove and return the element with the highest priority (root of the heap).
        
        Returns:
            The element removed from the priority queue.
        
        Raises:
            Exception: If the queue is empty.
        """
        if len(self) == 0:
            raise Exception("Underflow")
        to_dequeue = self.data.peek()
        self.data.delete(to_dequeue)
        return to_dequeue


class Persona:
    """
    Represents a person with a name and age. The age is used for comparing persons
    (for example, in a priority queue).
    """

    def __init__(self, nombre="", edad=1):
        """
        Initialize a new Persona instance.

        Args:
            nombre (str, optional): The person's name.
            edad (int, optional): The person's age.
        """
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """
        Return a string representation of the Persona.

        Returns:
            str: A string representation showing the person's name and age.
        """
        return str({
            "Nombre": self.nombre,
            "Edad": self.edad
        })

    def __lt__(self, other):
        """
        Define the 'less than' comparison based on age.

        Args:
            other (Persona): Another Persona to compare with.
        
        Returns:
            bool: True if this Persona's age is less than the other's; otherwise, False.
        """
        return self.edad < other.edad

# Global constants to define bounds and queue size.
MAX_BOUND = 72
MIN_BOUND = 18
SIZE = 10

def heapSort(lst):
    """
    Sort a list of elements using a priority queue based on a heap.

    The function builds a priority queue from the list, then repeatedly dequeues the
    highest-priority element and inserts it at the beginning of a result list.
    This results in the list being sorted in ascending order (assuming a max-heap
    and insertion at the beginning).

    Args:
        lst (list): The list of elements to sort.
    
    Returns:
        list: The sorted list.
    """
    result = []
    pq = PriorityQueue(lst)
    while len(pq) > 0:
        result.insert(0,pq.dequeue())
    return result

def main():
    """
    Demonstrate the usage of the PriorityQueue and heapSort functions using Persona objects.
    
    The main function:
      - Creates a list of Persona objects with random ages.
      - Initializes a PriorityQueue with these Persona objects.
      - Prints the original list of Persona objects.
      - Dequeues and prints each Persona from the PriorityQueue.
      - Uses heapSort to sort the original list and prints the sorted result.
    """
    lst = [Persona(uuid.uuid1(), randint(MIN_BOUND, MAX_BOUND)) for e in range(SIZE)]
    pq = PriorityQueue(lst)
    print(list(map(str, lst)))
    while len(pq) > 0:
        print('Atendiendo al cliente con edad ... ', pq.dequeue())
    print(list(map(str, heapSort(lst))))


if __name__ == "__main__":
    main()