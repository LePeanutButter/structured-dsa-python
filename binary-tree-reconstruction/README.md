# Binary Tree Reconstruction Using Traversals

## Introduction
This project reconstructs a binary tree using two traversal strings provided via standard input: the pre-order and in-order traversals. Once the tree is built, a post-order traversal is executed to produce the final output.

The idea is based on the classic observation that the first element in the pre-order traversal is the root of the tree, and the in-order traversal splits the tree into left and right subtrees. By recursively applying this concept, we reconstruct the binary tree and then traverse it in post-order.

## Input / Output Overview

**Input:**
- A single line of text containing two strings separated by whitespace:
  - The first string represents the pre-order traversal.
  - The second string represents the in-order traversal.

**Output:**
- The post-order traversal string of the reconstructed binary tree is printed on standard output.
