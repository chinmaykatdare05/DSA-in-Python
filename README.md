# Data Structures Implemented in Python

## Overview

This project implements various fundamental data structures in Python, including:

- Linked List (Singly & Doubly)
- Stack
- Queue
- Binary Search Tree
- Heap (Min-Heap)
- Trie
- Graph (Directed & Undirected)

Each data structure is implemented with core functionalities and methods for manipulation, insertion, deletion, and traversal.

---

## Implemented Data Structures & Functionalities

### 1. Linked List

#### **Singly Linked List**

- `append(data)`: Add an element to the end.
- `prepend(data)`: Add an element at the beginning.
- `insert(data, index)`: Insert an element at a specific index.
- `delete(data)`: Remove an element by value.
- `pop()`: Remove the last element.
- `remove(index)`: Remove an element by index.
- `getVal(index)`: Retrieve a value at an index.
- `setVal(index, data)`: Update a value at an index.
- `__repr__()`: String representation of the list.

#### **Doubly Linked List (Extended)**

- Similar to Singly Linked List but includes `prev` pointers for efficient bidirectional traversal.

---

### 2. Stack (LIFO)

- `push(data)`: Add an element to the stack.
- `pop()`: Remove and return the top element.
- `peek()`: Retrieve the top element without removing it.
- `is_empty()`: Check if the stack is empty.
- `__repr__()`: String representation of the stack.

---

### 3. Queue (FIFO)

- `enqueue(data)`: Add an element to the rear.
- `dequeue()`: Remove and return the front element.
- `peek()`: Retrieve the front element without removing it.
- `is_empty()`: Check if the queue is empty.
- `__repr__()`: String representation of the queue.

---

### 4. Binary Search Tree (BST)

- `insert(data)`: Insert a new node.
- `delete(data)`: Remove a node.
- `search(data)`: Check if a value exists.
- `in_order()`, `pre_order()`, `post_order()`: Different tree traversal methods.
- `height()`: Find the height of the tree.
- `is_balanced()`: Check if the tree is balanced.
- `is_bst()`: Validate if the structure satisfies BST properties.

---

### 5. Heap (Min-Heap)

- `insert(data)`: Insert an element while maintaining heap order.
- `extract_min()`: Remove and return the smallest element.
- `peek()`: Retrieve the smallest element without removal.
- `heapify(index)`: Maintain heap order.
- `meld(other_heap)`: Merge another heap.

---

### 6. Trie (Prefix Tree)

- `insert(word)`: Insert a word.
- `search(word)`: Check if a word exists.
- `delete(word)`: Remove a word from the Trie.
- `starts_with(prefix)`: Check if any word starts with a given prefix.

---

### 7. Graph (Directed & Undirected)

- `add_node(node)`: Add a node.
- `add_edge(node1, node2)`: Add an edge.
- `remove_node(node)`: Remove a node and its connections.
- `remove_edge(node1, node2)`: Remove an edge.
- `has_node(node)`, `has_edge(node1, node2)`: Check existence.
- `depth_first_search(start)`: Perform DFS.
- `breadth_first_search(start)`: Perform BFS.
- `shortest_path(start, end)`: Find the shortest path.
- `dijkstra(start)`: Compute shortest paths from a node.
- `topological_sort()`: Perform topological sorting.
- `is_cyclic()`: Detect cycles.
- `connected_components()`: Find connected components.
- `minimum_spanning_tree()`: Generate MST.
- `to_adjacency_matrix()`: Convert graph to an adjacency matrix.
