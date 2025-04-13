import random
import math

WHITE = "white"
BLACK = "black"
GRAY = "gray"

class Graph:
    """
    Represents a graph defined by a set of vertices and relationships (edges).
    Provides methods to construct both an adjacency list and an adjacency matrix,
    as well as graph traversal algorithms (BFS and DFS).
    """

    def __init__(self, vertexes, relations, directed=True, view=True):
        """
        Initializes the Graph with vertices, relations, and settings.

        Args:
            vertexes (list): List of vertices.
            relations (list): List of relations (edges) as tuples (start, end).
            directed (bool): True if the graph is directed.
            view (bool): If True, neighbor retrieval uses the adjacency list;
                         if False, uses the adjacency matrix.
        """
        self.directed = directed
        self.view = view
        self.vertexes = vertexes
        self.relations = relations
        self._buildAdjList()
        self._buildEncoding()
        self._buildAdjMatrix()

    def _buildAdjMatrix(self):
        """
        Builds an adjacency matrix representation of the graph.
        Each cell is set to 1 if there is an edge between the corresponding vertices.
        """
        self.adjMat = [[0 for _ in range(len(self.vertexes))] for _ in range(len(self.vertexes))]
        for relation in self.relations:
            row, col = self.encoder[relation[0]], self.encoder[relation[1]]
            self.adjMat[row][col] = 1

    def _buildEncoding(self):
        """
        Builds encoding and decoding dictionaries to map vertices to indices for
        the matrix representation.
        """
        self.encoder, self.decoder = {}, {}
        index = 0
        for v in self.vertexes:
            self.encoder[v] = index
            self.decoder[index] = v
            index += 1

    def _buildAdjList(self):
        """
        Constructs an adjacency list representation for the graph.
        """
        self.adjList = {}
        for v in self.vertexes:
            self.adjList[v] = []
        for relation in self.relations:
            self.adjList[relation[0]].append(relation[1])

    def _buildRelation(self, e):
        """
        Constructs the relations for the graph. For undirected graphs,
        adds both (u, v) and (v, u).

        Args:
            e (iterable): Iterable of relations (edges).
        """
        if self.directed:
            self.relations = e
        else:
            self.relations = set()
            for el in e:
                self.relations.add(el)
                self.relations.add((el[1], el[0]))

    def _init_(self, v, e, directed=True, view=True):
        """
        Alternative initializer to set up the graph with new vertices and relations.
        
        Args:
            v (list): List of vertices.
            e (list): List of relations (edges).
            directed (bool): Graph directionality.
            view (bool): Neighbor retrieval method.
        """
        self.directed = directed
        self.view = view
        self.vertexes = v
        self._buildRelation(e)
        self._buildAdjList()
        self._buildEncoding()
        self._buildAdjMatrix()

    def getAdjMatrix(self):
        """
        Returns the current adjacency matrix.
        
        Returns:
            list: The adjacency matrix.
        """
        return self.adjMat

    def getAdjList(self):
        """
        Returns the current adjacency list.
        
        Returns:
            dict: The adjacency list.
        """
        return self.adjList

    def _buildVProps(self, source=None):
        """
        Initializes vertex properties for graph traversals.
        
        Each vertex is given a color (for traversal), an infinite distance by default,
        and a null parent pointer. If a source is provided, its distance is set to 0.

        Args:
            source: The source vertex to initialize with distance 0.
        """
        self.v_props = {}
        for v in self.vertexes:
            self.v_props[v] = {
                'color': WHITE,
                'distance': math.inf,
                'parent': None
            }
        if source is not None:
            self.v_props[source] = {
                'color': GRAY,
                'distance': 0,
                'parent': None
            }

    def _getNeighborsAdjList(self, vertex):
        """
        Retrieves the neighbors of a vertex using the adjacency list.
        
        Args:
            vertex: The vertex for which to get neighbors.
        
        Returns:
            list: List of neighbor vertices.
        """
        return self.adjList[vertex]

    def _getNeighborsMatAdj(self, vertex):
        """
        Retrieves the neighbors of a vertex using the adjacency matrix.
        
        Args:
            vertex (int): The index corresponding to the vertex.
        
        Returns:
            list: List of neighbor vertices based on the matrix.
        """
        neighbors = []
        for i, cell in enumerate(self.adjMat[vertex]):
            if cell == 1:
                neighbors.append(self.decoder[i])
        return neighbors

    def getNeighbors(self, vertex):
        """
        Returns the neighbors of a given vertex based on the setting defined by `view`.

        Args:
            vertex: The vertex to query.
        
        Returns:
            list: List of neighboring vertices.
        """
        if self.view:
            return self._getNeighborsAdjList(vertex)
        return self._getNeighborsMatAdj(vertex)

    def bfs(self, source):
        """
        Performs a Breadth-First Search (BFS) starting from the specified source vertex.
        
        Args:
            source: The starting vertex for BFS.
        
        Returns:
            dict: A dictionary containing properties for each vertex (color, distance, parent).
        """
        self._buildVProps(source)
        queue = [source]
        while len(queue) > 0:
            u = queue.pop(0)
            for neighbor in self.getNeighbors(u):
                if self.v_props[neighbor]['color'] == WHITE:
                    self.v_props[neighbor]['color'] = GRAY
                    self.v_props[neighbor]['distance'] = self.v_props[u]['distance'] + 1
                    self.v_props[neighbor]['parent'] = u
                    queue.append(neighbor)
            self.v_props[u]['color'] = BLACK
        return self.v_props

    def dfs(self):
        """
        Performs a Depth-First Search (DFS) over the entire graph.
        
        Returns:
            dict: A dictionary of vertex properties including discovery and finish times.
        """
        self._buildVProps()
        time = 0
        for v in self.vertexes:
            if self.v_props[v]['color'] == WHITE:
                time = self.dfs_visit(v, time)
        return self.v_props

    def dfs_visit(self, vertex, time):
        """
        Recursively visits vertices for DFS.
        
        Args:
            vertex: The vertex being visited.
            time (int): The current time counter.
        
        Returns:
            int: Updated time after processing the vertex and its descendants.
        """
        time += 1
        self.v_props[vertex]['distance'] = time
        self.v_props[vertex]['color'] = GRAY
        for neighbor in self.getNeighbors(vertex):
            if self.v_props[neighbor]['color'] == WHITE:
                self.v_props[neighbor]['parent'] = vertex
                time = self.dfs_visit(neighbor, time)
        self.v_props[vertex]['color'] = BLACK
        time += 1
        self.v_props[vertex]['final'] = time
        return time

def printVProps(v_props):
    """
    Prints vertex properties including the optimal path from the source vertex.
    
    Args:
        v_props (dict): Dictionary containing properties for each vertex.
    """
    print("===================== Results =======================")
    for v in v_props.keys():
        v_props[v]['path'] = '-->'.join(map(str, getPath(v, v_props)))
        print("Optimal path from", str(v), ":", v_props[v])

def printAdjMatrix(graph):
    """
    Prints the graph's adjacency matrix.
    
    Args:
        graph (Graph): The Graph instance.
    """
    print("===================== Adjacency Matrix =======================")
    adjMat = graph.getAdjMatrix()
    for row in adjMat:
        print(' '.join(list(map(str, row))))

def getPath(vertex, v_props):
    """
    Reconstructs the path from the source to the given vertex using parent pointers.
    
    Args:
        vertex: The target vertex.
        v_props (dict): Dictionary of vertex properties.
    
    Returns:
        list: The path from the source to the target vertex.
    """
    path = [vertex]
    current = vertex
    while v_props[current]['parent'] is not None:
        path.insert(0, v_props[current]['parent'])
        current = v_props[current]['parent']
    return path

def printAdjList(graph):
    """
    Prints the graph's adjacency list.
    
    Args:
        graph (Graph): The Graph instance.
    """
    print("===================== Adjacency List =======================")
    adjList = graph.getAdjList()
    for v in adjList.keys():
        print(str(v), list(map(str, adjList[v])))

def generate_labyrinth(rows, cols, max_number):
    """
    Generates a labyrinth represented as a 2D grid of random integers.
    
    Args:
        rows (int): Number of rows in the labyrinth.
        cols (int): Number of columns in the labyrinth.
        max_number (int): Maximum possible number in a cell.
    
    Returns:
        list: A 2D list representing the labyrinth.
    """
    labyrinth = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(0, max_number))
        labyrinth.append(row)
    return labyrinth

def convert_to_graph(labyrinth):
    """
    Converts a labyrinth (2D grid) into a graph where cells with nonzero values are vertices.
    Edges are added between adjacent cells (up, down, left, right) if both cells are nonzero.
    
    Args:
        labyrinth (list): A 2D list representing the labyrinth.
    
    Returns:
        Graph: A graph constructed from the labyrinth.
    """
    vertexes = []
    relations = []
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    for i in range(rows):
        for j in range(cols):
            if labyrinth[i][j] != 0:  # Non-wall cell
                vertexes.append((i, j))
                # Check for neighbors and add relations if both cells are accessible
                if i > 0 and labyrinth[i - 1][j] != 0:  # Upper neighbor
                    relations.append(((i, j), (i - 1, j)))
                if i < rows - 1 and labyrinth[i + 1][j] != 0:  # Lower neighbor
                    relations.append(((i, j), (i + 1, j)))
                if j > 0 and labyrinth[i][j - 1] != 0:  # Left neighbor
                    relations.append(((i, j), (i, j - 1)))
                if j < cols - 1 and labyrinth[i][j + 1] != 0:  # Right neighbor
                    relations.append(((i, j), (i, j + 1)))
    return Graph(vertexes, relations)

def main():
    """
    Main function to demonstrate the conversion of a labyrinth into a graph,
    and perform BFS and DFS to find an optimal path to a target number.
    """
    rows = 5
    cols = 5
    max_number = 6  # Maximum number in any cell
    target_number = 6  # Target number to locate in the labyrinth

    laberinto = generate_labyrinth(rows, cols, max_number)
    print("Generated Labyrinth:")
    for row in laberinto:
        print(row)

    graph = convert_to_graph(laberinto)

    print("\nUsing BFS to find the optimal path to the number", target_number)
    for v in graph.vertexes:
        if laberinto[v[0]][v[1]] == target_number:
            bfs_result = graph.bfs(v)
            printVProps(bfs_result)
            break

    print("\nUsing DFS to find the optimal path to the number", target_number)
    for v in graph.vertexes:
        if laberinto[v[0]][v[1]] == target_number:
            dfs_result = graph.dfs()
            printVProps(dfs_result)
            break

if __name__ == "__main__":
    main()
