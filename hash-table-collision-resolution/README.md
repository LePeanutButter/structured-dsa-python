# Hash Table Collision Resolution Strategies

## Overview
This repository contains several implementations of a hash table that efficiently handles collisions using various strategies. The goal is to support fast insertion, deletion, and search operations even in worst-case scenarios. Different approaches are explored such as linked list chaining, binary search within indexed arrays, depth-first search (DFS), and the use of disjoint sets.

## Problem Description
We face the challenge of implementing a hash table that manages collisions efficiently. In a hash table, collisions occur when multiple keys hash to the same index. To resolve these collisions, we explore multiple strategies:

- **Linked List Chaining:**  
  Each bucket in the hash table is a linked list. When collisions occur, new elements are appended to the list corresponding to the hash index.

- **Binary Search in Indexed Arrays:**  
  Buckets are maintained as sorted arrays. In the event of a collision, a binary search is performed to identify the correct insertion point, allowing efficient lookup.

- **Depth-First Search (DFS):**  
  When a collision occurs, DFS is used to traverse an associated structure (such as a tree) to locate an available slot for the new element.

- **Disjoint Sets for Collision Handling:**  
  In this approach, along with storing key-value pairs in buckets, a disjoint set (union-find) structure is employed to merge related elements. This helps in grouping keys that hash to the same index, even when they have collided.

## Input and Output

### Input
- **Elements to Insert:**  
  Records representing, for example, export data including destination country, export date, and coffee company with its price.
  
- **Elements to Search:**  
  Keys used to locate elements in the hash table.

- **Elements to Delete:**  
  Keys to be removed from the hash table.

### Output
- **Search Results:**  
  Output will indicate whether a key is found (found/not found).
  
- **Deletion Outcomes:**  
  Operation success (or error if the element does not exist).

- **Final State:**  
  Information on the final state of the hash table. For the disjoint sets implementation, the connected components (merged keys) are displayed.

## Strategies and Implementation Details

### 1. Linked List Chaining
- **Strategy:**  
  Use separate chaining where each hash table slot maintains a linked list for colliding entries.
- **Advantages:**  
  - Efficient collision handling even with many colliding items.
  - Dynamic memory usage, as lists grow and shrink as needed.
- **Disadvantages:**  
  - Increased memory overhead due to the storage of pointers.
  - Worst-case operations (insertion, search, deletion) become linear if all keys end up in the same list.

### 2. Binary Search in Indexed Arrays
- **Strategy:**  
  Use a sorted list (indexed array) for each bucket. Upon collision, a binary search is performed to quickly locate the desired position.
- **Advantages:**  
  - Binary search offers O(log n) performance within a bucket.
  - Potentially lower memory usage when the hash table size is small.
- **Disadvantages:**  
  - Requires maintaining sorted order, which can add complexity.
  - Efficiency depends on the array size; too large an array increases memory demands, too small may cause excessive collisions.

### 3. Depth-First Search (DFS)
- **Strategy:**  
  When collisions occur, DFS is used to traverse an associated data structure (e.g., a tree) to determine where the new element should be inserted.
- **Advantages:**  
  - Guarantees an insertion position will be found even under heavy collision scenarios.
  - Flexible in handling different underlying data structures.
- **Disadvantages:**  
  - More complex to implement than simpler collision resolution strategies.
  - May incur extra computational overhead.

### 4. Disjoint Sets for Collision Handling
- **Strategy:**  
  Integrate a disjoint set (union-find) structure with the hash table. Each bucket’s key-value pair is merged with related keys through union operations, keeping track of connected components.
- **Advantages:**  
  - Efficient union and search (find) operations.
  - Excellent for handling multiple collisions by grouping related entries.
- **Disadvantages:**  
  - Integration complexity and extra memory overhead.
  - The union operation may add computational cost, particularly with large colliding sets.

## Test Cases
The provided implementations are tested using sample export data that includes:
- A tuple comprising export details (destination country, export date, coffee company).
- A numeric export value (price).

The test cases involve:
- Insertion of multiple export records.
- Searching for specific records.
- Deletion where applicable.
- Reporting the final state of the data structure and, if using disjoint sets, the final connected components.
- Performance measurement (e.g., execution time).
