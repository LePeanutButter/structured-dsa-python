# Linked List-Based LIFO Stack Implementation

## Overview
This repository provides an implementation of a LIFO (Last-In, First-Out) stack using linked lists in Python. The code demonstrates the use of linked lists—an essential data structure for dynamic data manipulation—by creating a stack that efficiently supports push and pop operations. In addition, it uses object-oriented programming principles to represent books through a dedicated `Book` class.

## Introduction
In this lab, we explore linked lists and their application in implementing an LIFO stack. Linked lists allow for dynamic insertion and deletion of elements without requiring contiguous memory allocation, which is ideal for structures such as stacks where elements are frequently added and removed.

## Linked Lists
A linked list is a dynamic data structure composed of nodes. Each node contains:
- **A data element:** In our case, a `Book` object.
- **A pointer to the next node:** This pointer links nodes together, forming the list.

This approach offers the flexibility to insert or delete elements quickly—in O(n) time in the worst case—without the need for large contiguous memory blocks.

## Object-Oriented Programming and Classes
The implementation leverages object-oriented programming (OOP) by defining classes that encapsulate data and behavior:
- **`Book` Class:**  
  Defines a book with attributes such as a unique code, title, description, and publication year.
- **`Node` Class:**  
  Implements the fundamental building block for the linked list. Each node holds a `Book` instance and a pointer to the next node.
- **`LinkedListStack` Class:**  
  Implements a LIFO stack using a singly linked list. The stack supports:
  - **Push:** Adding a new element at the top.
  - **Pop:** Removing the top element.
  - **Peek:** Viewing the element at the top without removing it.

## LIFO Stack - Last In, First Out
A LIFO stack is a data structure where the last element added is the first one to be removed. Using a linked list for this purpose allows:
- Efficient addition (push) of new elements at the top.
- Efficient removal (pop) of the top element.
- Access to the top element (peek) without altering the stack.

## Representation of Book Information
For managing book information, the following attributes are encapsulated in the `Book` class:
1. **Code:** A unique identifier for each book, auto-generated using `uuid4`.
2. **Name:** The title of the book.
3. **Description:** A brief synopsis of the book.
4. **Year of Publication:** The year the book was released.

Each book instance organizes these attributes internally, ensuring structured and consistent data management.