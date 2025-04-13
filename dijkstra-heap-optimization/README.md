# Optimization of Dijkstra's Algorithm Through Binary Heap and HeapSort

## Introduction
This project focuses on making Dijkstra's algorithm more efficient for finding the shortest path in a weighted graph. To achieve this, we first ensure that our binary heap—a key data structure used in Dijkstra's algorithm—is fully optimized. In particular, we complete the implementation of the `min_heapify` function. In addition, we adapt a sorting method called HeapSort to work with our binary heap in both its minimal (min-heap) and maximal (max-heap) forms.

The binary heap functions like an ordered list where the smallest element is always kept at the top. This property is crucial for Dijkstra's algorithm because it allows us to quickly extract the vertex with the smallest distance at each step. HeapSort, being an efficient sorting algorithm, is adapted in this project to work with either version of the binary heap, ensuring our data can be sorted quickly and effectively.

Finally, the optimized binary heap structure is integrated into Dijkstra's algorithm. Rather than using a traditional `extract_min` function, we utilize our custom priority queue based on the binary heap. This modification dramatically improves the performance of the algorithm when determining the vertex with the shortest distance.

## Problems Addressed
The project tackles the following challenges:
- **Implementing the minimal binary heap:** Complete the `min_heapify` function to maintain a valid min-heap.
- **Implementing HeapSort functions:** Adapt HeapSort for both the minimal and maximal versions of the binary heap.
- **Optimizing Dijkstra's algorithm:** Replace the standard extract-min functionality with a priority queue based on the optimized binary heap to determine the vertex with the smallest distance.
- **Testing:** Provide test cases to validate the prototype.

## Input
The inputs for this project are:
- **A list of vertices:** Represented by objects of type `Persona`, where each person (vertex) has a name and an age.
- **A list of directed edges:** Each edge is a tuple containing the name of the start vertex, the name of the destination vertex, and the weight of that relationship (edge).

## Output
The outputs produced by the system are:
- **The graph's adjacency matrix:** A matrix representation of the graph where each entry indicates the weight of an edge.
- **The graph's adjacency list:** A list representation of the graph where each vertex is mapped to its neighbors along with the corresponding edge weights.
- **Dijkstra's Algorithm Result:** The output includes the shortest distance and the corresponding shortest path from the source vertex to all other vertices in the graph.

## Sample Test Cases
The project has been validated with various scenarios, including:
- **A regular connection** between two different vertices, resulting in a specific edge weight.
- **A self-loop**, where a vertex connects to itself with a defined weight.
- **An edge with zero distance**, indicating no cost or distance between vertices.                |

## Project Structure
The repository contains modules that implement:
- A binary heap with both min-heap and max-heap capabilities.
- A priority queue built on top of the binary heap.
- A graph module that constructs both an adjacency matrix and list from given vertices and edges.
- Integration of Dijkstra's algorithm utilizing the optimized priority queue.
- Supporting algorithms (such as BFS and DFS) and helper functions to display and reconstruct graph paths.