class MinHeap:
    def __init__(self):
        # Initialize an empty heap
        self.heap = []
        self.size = 0

    def __repr__(self):
        # Time Complexity: O(n)
        return " → ".join(map(str, self.heap))

    def __len__(self):
        # Time Complexity: O(1)
        return self.size

    def __contains__(self, data):
        # Time Complexity: O(n)
        return data in self.heap

    def insert(self, data):
        # Time Complexity: O(log n)
        self.heap.append(data)  # Add the element to the end
        self.size += 1
        self.sift_up(self.size - 1)  # Restore the min-heap property

    def peek(self):
        # Time Complexity: O(1)
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]  # Return the smallest element (root)

    def extract_min(self):
        # Time Complexity: O(log n)
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.delete(0)  # Remove and return the root element

    def is_empty(self):
        # Time Complexity: O(1)
        return self.size == 0

    def heapify(self, index):
        # Time Complexity: O(log n)
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index

        # Find the smallest among root, left child, and right child
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and recurse
        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.heapify(smallest)

    def parent(self, index):
        # Time Complexity: O(1)
        return (index - 1) // 2 if index > 0 else None

    def left_child(self, index):
        # Time Complexity: O(1)
        return 2 * index + 1

    def right_child(self, index):
        # Time Complexity: O(1)
        return 2 * index + 2

    def meld(self, other):
        # Time Complexity: O(n log n)
        self.heap.extend(other.heap)  # Merge the two heaps
        self.size += other.size
        # Rebuild the min-heap property
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)

    def delete(self, index):
        # Time Complexity: O(log n)
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        # Swap the element to delete with the last element
        self.heap[index], self.heap[self.size - 1] = (
            self.heap[self.size - 1],
            self.heap[index],
        )
        data = self.heap.pop()  # Remove the last element
        self.size -= 1

        # Restore the min-heap property
        if index < self.size:
            self.sift_down(index)
            self.sift_up(index)

        return data

    def sift_up(self, index):
        # Time Complexity: O(log n)
        parent = self.parent(index)
        # Swap with parent if the current element is smaller
        if parent is not None and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.sift_up(parent)

    def sift_down(self, index):
        # Time Complexity: O(log n)
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index

        # Find the smallest among root, left child, and right child
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and recurse
        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.sift_down(smallest)


if __name__ == "__main__":
    # Initialize a MinHeap
    h = MinHeap()
    print("Heap initialized:", h)
    print("Is heap empty?", h.is_empty())

    # Insert elements
    h.insert(5)
    h.insert(3)
    h.insert(8)
    h.insert(1)
    h.insert(4)
    print("Heap after inserts:", h)

    # Test peek
    print("Peek (min element):", h.peek())

    # Test extract_min
    print("Extracted min:", h.extract_min())
    print("Heap after extracting min:", h)

    # Test delete
    print("Deleting element at index 1 (value 4):", h.delete(1))
    print("Heap after deletion:", h)

    # Test contains
    print("Is 8 in the heap?", 8 in h)
    print("Is 10 in the heap?", 10 in h)

    # Test melding two heaps
    other_heap = MinHeap()
    other_heap.insert(7)
    other_heap.insert(2)
    print("Other heap:", other_heap)
    h.meld(other_heap)
    print("Heap after melding with other heap:", h)

    # Test __len__
    print("Heap size:", len(h))

    # Extract all elements to empty the heap
    while not h.is_empty():
        print("Extracted min:", h.extract_min(), " | Remaining heap:", h)

    # Final heap state
    print("Is heap empty after extracting all elements?", h.is_empty())
    print("Final heap state:", h)
