# Labyrinth Graph Search: BFS and DFS Algorithms

## Introduction
In this laboratory, we dive into the fascinating world of depth-first search (DFS) and breadth-first search (BFS) algorithms. These search algorithms are fundamental tools for solving a wide range of problems—from network navigation to optimal route planning. The primary goal is to build a functional prototype addressing a real-life scenario using these techniques. We explore questions such as:
- How to find the shortest route from point A to point B?
- How to explore a labyrinth to find the fastest exit?

In this report, we present our designs and solutions for these challenges. We explore both DFS, which delves deep into a problem before backtracking, and BFS, which simultaneously explores all possible solutions to efficiently determine the optimal one. Additionally, test cases are provided to demonstrate the prototype's functionality and effectiveness in various scenarios.

## Strategy
Our approach is based on transforming a randomly generated labyrinth into a graph. In this process:
- **Graph Construction:** Every cell of the labyrinth becomes a vertex, and connections (edges) are established between adjacent cells—excluding those blocked by walls.
- **Target Identification:** A specific cell value (target_number) is set as the objective. 
- **Path Search:** Both BFS and DFS algorithms are applied to determine optimal paths from the cell containing the target_number to all other cells that also hold that number.
  - **BFS** ensures the shortest and most efficient route is identified.
  - **DFS** exhaustively explores all potential paths.
- Finally, we compare the number and length of the paths found by both algorithms to decide on the optimal solution in terms of efficiency and resource usage.

This systematic and efficient approach provides a robust solution for finding the best path in a randomly generated labyrinth.

## Inputs
- **Rows:** Number of rows in the labyrinth.
- **Cols:** Number of columns in the labyrinth.
- **Max_number:** The maximum value that can appear in any cell of the labyrinth.
- **Target_number:** The specific value to be found in the labyrinth.

## Output
The output is the optimal path (or paths) from any cell containing the target_number to all other cells with that value, determined using both breadth-first (BFS) and depth-first (DFS) search algorithms.

## Example Test Cases

- **Case 1:**
  - **Input:** (1, 2, 3, 4)
  - **Justification:** A non-square matrix where the maximum number is less than the target number.
  - **Expected Output:** NULL (no valid path exists)

- **Case 2:**
  - **Input:** (5, 5, 6, 6)
  - **Justification:** A square matrix where the target_number equals the maximum number.
  - **Expected Output:** 24 paths found using BFS and 22 paths found using DFS

- **Case 3:**
  - **Input:** (5, 5, 4, 3)
  - **Justification:** A square matrix with a maximum number that is less than the number of rows, resulting in the target_number being less than the maximum.
  - **Expected Output:** 19 paths found using both BFS and DFS

## Overview of the Project Content
This repository contains modules that:
- Generate a labyrinth (2D grid) using random values.
- Convert the labyrinth into a graph where each accessible cell (nonzero value) becomes a vertex.
- Build graph representations (both an adjacency list and an adjacency matrix) from the labyrinth.
- Apply BFS and DFS algorithms to search for optimal paths from cells containing the target number.
- Include helper functions for printing the graph representations and reconstructing paths.
