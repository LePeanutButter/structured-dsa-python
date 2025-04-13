from collections import deque
import math
from random import randint

WHITE = "white"
BLACK = "black"
GRAY = "gray"

class Graph:
    """
    Represents a weighted graph with support for multiple representations:
    - Adjacency Matrix
    - Adjacency List
    - Vertex encoding (to map vertices to indices).

    The graph can be directed or undirected. It also provides methods for common
    graph algorithms such as Dijkstra's algorithm, Breadth-First Search (BFS), and
    Depth-First Search (DFS).
    """
    
    def _buildAdjMatrix(self):
        """
        Build an adjacency matrix for the graph using the vertex encoding.
        
        The matrix is constructed as a 2D list (size n x n) initialized with zeros.
        For each relation, the corresponding entry (row, col) is updated with the
        weight of the edge.
        """
        self.adjMat = [[0 for v in range(len(self.vertexes))] for v in range(len(self.vertexes))]
        for relation in self.relations:
            row, col = self.encoder[relation[0]], self.encoder[relation[1]]
            self.adjMat[row][col] = relation[2]  # Use the edge weight in the adjacency matrix

    def _buildEncoding(self):
        """
        Build encoding and decoding dictionaries to map vertices to indices and vice versa.
        
        This is useful for representing the graph as an adjacency matrix.
        """
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index += 1

    def _buildAdjList(self):
        """
        Build an adjacency list representation of the graph.
        
        The adjacency list is a dictionary where each vertex maps to a list of 
        tuples containing (neighbor_vertex, edge_weight).
        """
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append((relation[1], relation[2]))  # Store weight along with neighbor

    def _buildRelation(self, e):
        """
        Build the graph relation (edges) based on whether the graph is directed or not.
        
        For undirected graphs, both (u, v, weight) and (v, u, weight) are added.
        
        Args:
            e (iterable): List or set of tuples, where each tuple represents an edge.
        """
        if self.directed:
            self.relations = e
        else:
            self.relations = set()
            for el in e:
                self.relations.add(el)
                if len(el) == 3:
                    self.relations.add((el[1], el[0], el[2]))

    def __init__(self, v, e, directed=True, view=True):
        """
        Initialize the Graph object.
        
        Args:
            v (list): The list of vertices.
            e (iterable): The list of edges. Each edge is a tuple (source, destination, weight).
            directed (bool, optional): True if the graph is directed, otherwise False.
            view (bool, optional): If True, the graph's construction is intended to be visible in some output.
        """
        self.directed = directed
        self.view = view
        self.vertexes = v
        self._buildRelation(e)
        self._buildAdjList()
        self._buildEncoding()
        self._buildAdjMatrix()
        self._buildWeight()

    def _buildWeight(self):
        """
        Build a dictionary mapping each edge (as a tuple (u, v)) to its weight.
        """
        self._weight = {}
        for relation in self.relations:
            self._weight[(relation[0], relation[1])] = relation[2]

    def getAdjMatrix(self):
        """
        Retrieve the adjacency matrix representation of the graph.
        
        Returns:
            list: The adjacency matrix.
        """
        return self.adjMat

    def getAdjList(self):
        """
        Retrieve the adjacency list representation of the graph.
        
        Returns:
            dict: The adjacency list.
        """
        return self.adjList

    def dijkstraP(self, s):
        """
        Compute shortest paths from the source vertex 's' to all other vertices using
        Dijkstra's algorithm and a priority queue (min-heap).
        
        Args:
            s: The source vertex.
        
        Returns:
            dict: A dictionary where each key is a vertex and the value is a dictionary
                  with properties: distance (shortest path length), parent, etc.
        """
        self._buildVProps(s)
        QS = PriorityQueue([(self.v_props[v]['distance'], v) for v in self.vertexes], config=False)  # Min-Heap
        in_queue = {v: True for v in self.vertexes}  # Track vertices in the queue
        while len(QS) > 0:
            u = QS.dequeue()[1]
            in_queue[u] = False  # Mark as dequeued
            for neighbor, weight in self.getNeighbors(u):
                if self.v_props[neighbor]['distance'] > self.v_props[u]['distance'] + weight:
                    old_distance = self.v_props[neighbor]['distance']
                    self.v_props[neighbor]['distance'] = self.v_props[u]['distance'] + weight
                    self.v_props[neighbor]['parent'] = u
                    if in_queue[neighbor]:
                        QS.update((old_distance, neighbor), (self.v_props[neighbor]['distance'], neighbor))
        return self.v_props

    def _buildVProps(self, source=None):
        """
        Initialize the vertex properties for search algorithms.
        
        For each vertex, set default properties: color (for traversal), distance (infinity),
        and parent (None). If a source vertex is provided, its distance is set to 0.
        
        Args:
            source: The source vertex for algorithms like BFS or Dijkstra.
        """
        self.v_props = {}
        for v in self.vertexes:
            self.v_props[v] = {
                'color': WHITE,
                'distance': math.inf,
                'parent': None
            }
        if source is not None:
            self.v_props[source]['distance'] = 0

    def _getNeighborsAdjList(self, vertex):
        """
        Retrieve the list of neighbors for a given vertex using the adjacency list.
        
        Args:
            vertex: The vertex whose neighbors are to be retrieved.
        
        Returns:
            list: A list of tuples, each containing (neighbor, weight).
        """
        return self.adjList[vertex]

    def getNeighbors(self, vertex):
        """
        Get the neighbors for a given vertex.
        
        Args:
            vertex: The vertex to query.
        
        Returns:
            list: Neighbors of the vertex (as (neighbor, weight) pairs).
        """
        return self._getNeighborsAdjList(vertex)

    def bfs(self, source):
        """
        Perform Breadth-First Search (BFS) starting from the source vertex.
        
        During BFS, each vertex is labeled with a distance from the source and a parent.
        
        Args:
            source: The starting vertex.
        
        Returns:
            dict: The vertex properties after BFS, including color, distance, and parent.
        """
        self._buildVProps(source)
        queue = [source]
        while len(queue) > 0:
            u = queue.pop(0)
            for neighbor, _ in self.getNeighbors(u):
                if self.v_props[neighbor]['color'] == WHITE:
                    self.v_props[neighbor]['color'] = GRAY
                    self.v_props[neighbor]['distance'] = self.v_props[u]['distance'] + 1
                    self.v_props[neighbor]['parent'] = u
                    queue.append(neighbor)
            self.v_props[u]['color'] = BLACK
        return self.v_props

    def dfs(self):
        """
        Perform a Depth-First Search (DFS) over the graph.
        
        Each vertex is visited recursively and annotated with discovery and finish times.
        
        Returns:
            dict: The vertex properties after DFS.
        """
        self._buildVProps()
        time = 0
        for v in self.vertexes:
            if self.v_props[v]['color'] == WHITE:
                time = self.dfs_visit(v, time)
        return self.v_props

    def dfs_visit(self, vertex, time):
        """
        Recursively visit nodes in DFS starting from a given vertex.
        
        Args:
            vertex: The current vertex being visited.
            time (int): The current time counter for discovery/finish times.
        
        Returns:
            int: The updated time after exploring the vertex and its descendants.
        """
        time += 1
        self.v_props[vertex]['distance'] = time
        self.v_props[vertex]['color'] = GRAY
        for neighbor, _ in self.getNeighbors(vertex):
            if self.v_props[neighbor]['color'] == WHITE:
                self.v_props[neighbor]['parent'] = vertex
                time = self.dfs_visit(neighbor, time)
        self.v_props[vertex]['color'] = BLACK
        time += 1
        self.v_props[vertex]['final'] = time
        return time

def printVProps(v_props):
    """
    Print the properties of each vertex after running a graph algorithm.
    
    For each vertex, a path (from source to the vertex) is constructed and displayed.
    
    Args:
        v_props (dict): A dictionary containing vertex properties.
    """
    print("===================== Results =======================")
    for v in v_props.keys():
        v_props[v]['path'] = '-->'.join(map(str, getPath(v, v_props)))
        print(str(v), '-->', v_props[v])

def printAdjMatrix(graph):
    """
    Print the adjacency matrix of the graph.
    
    Args:
        graph (Graph): The Graph instance from which to obtain the matrix.
    """
    print("===================== ADJ Matrix =======================")
    adjMat = graph.getAdjMatrix()
    for row in adjMat:
        print(' '.join(list(map(str, row))))

def getPath(vertex, v_props):
    """
    Reconstruct the path from the source to the given vertex based on parent pointers.
    
    Args:
        vertex: The vertex to build the path for.
        v_props (dict): The dictionary containing vertex properties.
    
    Returns:
        list: The sequence of vertices from the source to the given vertex.
    """
    path = [vertex]
    current = vertex
    while v_props[current]['parent'] is not None:
        path.insert(0, v_props[current]['parent'])
        current = v_props[current]['parent']
    return path

def printAdjList(graph):
    """
    Print the adjacency list of the graph.
    
    Args:
        graph (Graph): The Graph instance from which to obtain the adjacency list.
    """
    print("===================== ADJ List =======================")
    adjList = graph.getAdjList()
    for v in adjList.keys():
        print(str(v), list(map(str, adjList[v])))

class Heap:
    """
    Implements a binary heap data structure that can act as a max-heap or min-heap,
    based on its configuration.
    """
    
    def __init__(self, data=[], config=True):
        """
        Initialize a new Heap instance.
        
        Args:
            data (list, optional): Initial list of elements.
            config (bool, optional): True for a max-heap; False for a min-heap.
        """
        self.data = []
        self.config = config
        self.build(data[:])

    def left(self, index):
        """
        Get the index of the left child for the given index.
        
        Args:
            index (int): The parent's index.
        
        Returns:
            int: The left child's index.
        """
        return 2 * index + 1

    def right(self, index):
        """
        Get the index of the right child for the given index.
        
        Args:
            index (int): The parent's index.
        
        Returns:
            int: The right child's index.
        """
        return 2 * (index + 1)

    def parent(self, index):
        """
        Get the index of the parent for the given index.
        
        Args:
            index (int): The child's index.
        
        Returns:
            int: The parent's index.
        """
        return (index - 1) // 2

    def height(self):
        """
        Compute the height of the heap.
        
        Returns:
            int: The height of the heap.
        """
        if len(self.data) == 0:
            return 0
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
        Insert a new element into the heap and rebuild the heap.
        
        Args:
            new: The new element to insert.
        """
        self.data.append(new)
        self.build()

    def update(self, old, new):
        """
        Update an element in the heap.
        
        This method finds the index of an element, replaces it with a new value,
        and heapifies from that index.
        
        Args:
            old: The old element to be updated.
            new: The new element to replace the old one.
        """
        try:
            index = self.data.index(old)
            self.data[index] = new
            self.heapify(index)
        except ValueError:
            # If 'old' is not in the heap, nothing is done.
            pass

    def delete(self, to_delete):
        """
        Delete an element from the heap and rebuild the heap.
        
        Args:
            to_delete: The element to remove.
        
        Raises:
            Exception: If the heap is empty or the element is not found.
        """
        if len(self) == 0:
            raise Exception("The heap is empty.")
        if to_delete not in self.data:
            raise Exception("The element is not in the heap.")
        self.data.remove(to_delete)
        self.build()

    def build(self, data=[]):
        """
        Build or rebuild the heap from a list of data.
        
        If a new data list is provided and is non-empty, it replaces the current data.
        Then, all non-leaf nodes are heapified to maintain the heap property.
        
        Args:
            data (list, optional): A new list of elements to build the heap from.
        """
        if data and isinstance(data, list) and len(data) > 0:
            self.data = data
        for index in range(len(self) // 2, -1, -1):
            self.heapify(index)

    def heapify(self, index):
        """
        Heapify the subtree rooted at the given index according to the heap configuration.
        
        Delegates to either max_heapify or min_heapify.
        
        Args:
            index (int): The index at which to start heapification.
        """
        if self.config:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def max_heapify(self, index):
        """
        Maintain the max-heap property for the subtree rooted at the given index.
        
        Args:
            index (int): The index to heapify.
        """
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

    def min_heapify(self, index):
        """
        Maintain the min-heap property for the subtree rooted at the given index.
        
        Args:
            index (int): The index to heapify.
        """
        left_index, right_index, smallest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[left_index] < self.data[smallest_index]:
            smallest_index = left_index
        if right_index < len(self) and self.data[right_index] < self.data[smallest_index]:
            smallest_index = right_index
        if smallest_index != index:
            self.data[smallest_index], self.data[index] = self.data[index], self.data[smallest_index]
            self.min_heapify(smallest_index)

    def peek(self):
        """
        Return the top element of the heap without removing it.
        
        Returns:
            The element at the root of the heap.
        """
        return self.data[0]

    def __str__(self):
        """
        Return a string representation of the heap.
        
        Returns:
            str: The underlying list representation of the heap.
        """
        return str(self.data)

class PriorityQueue:
    """
    Implements a priority queue using the Heap class.
    
    Provides enqueue, dequeue, and update operations based on the underlying heap.
    """
    
    def __init__(self, data=[], config=True):
        """
        Initialize the PriorityQueue.
        
        Args:
            data (list, optional): Initial list of elements.
            config (bool, optional): True for a max-heap; False for a min-heap.
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
            new: The new element to enqueue.
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

    def update(self, old, new):
        """
        Update an element within the priority queue.
        
        Args:
            old: The existing element.
            new: The new element to replace the old element.
        """
        self.data.update(old, new)

class Persona:
    """
    Represents a person with a name and age.
    
    The age attribute is used for comparison, which is useful for prioritization
    in the priority queue.
    """
    
    def __init__(self, nombre="", edad=1):
        """
        Initialize a new Persona.

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
            str: A string showing the name and age.
        """
        return str({
            "Nombre": self.nombre,
            "Edad": self.edad
        })

    def __lt__(self, other):
        """
        Define the less-than operator based on age.

        Args:
            other (Persona): Another Persona instance for comparison.

        Returns:
            bool: True if this Persona's age is less than the other's; otherwise, False.
        """
        return self.edad < other.edad

# Global constants used for generating random ages and setting queue size.
MAX_BOUND = 72
MIN_BOUND = 18
SIZE = 10

def heapSort(lst, config=True):
    """
    Sort a list using heap sort via the Heap data structure.

    Args:
        lst (list): The list of elements to sort.
        config (bool, optional): Heap configuration; True for max-heap, False for min-heap.

    Returns:
        list: The sorted list.
    """
    heap = Heap(lst, config)
    result = []
    while len(heap) > 0:
        result.append(heap.peek())
        heap.delete(heap.peek())
    return result

def main():
    """
    Demonstrate the usage of the graph and priority queue operations with Persona instances.
    
    The main function:
        - Creates a list of Persona objects with random ages.
        - Constructs a graph using the Persona names as vertices and sample relationships (with weights).
        - Prints the graph's adjacency matrix and adjacency list.
        - Runs Dijkstra's algorithm on the graph from a source vertex and displays the resulting vertex properties.
    """
    lst = [Persona(f'Persona {i}', randint(MIN_BOUND, MAX_BOUND)) for i in range(SIZE)]

    vertices = [persona.nombre for persona in lst]
    relaciones = [
        ('Persona 0', 'Persona 1', 0),
        ('Persona 0', 'Persona 2', 1),
        ('Persona 1', 'Persona 1', 1),
        ('Persona 2', 'Persona 1', 2),
        ('Persona 2', 'Persona 3', 5),
        ('Persona 3', 'Persona 4', 3)
    ]

    graph = Graph(vertices, relaciones, directed=True, view=True)

    printAdjMatrix(graph)
    printAdjList(graph)

    source_vertex = 'Persona 0'
    print("====================== Dijkstra using Priority Queue ===================")
    dijkstra_result = graph.dijkstraP(source_vertex)
    printVProps(dijkstra_result)

if __name__ == "__main__":
    main()