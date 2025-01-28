class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def __repr__(self):
        # Time Complexity: O(n)
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.data)
            cur = cur.next
        return " → ".join(map(str, res))

    def __contains__(self, data):
        # Time Complexity: O(n)
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def __len__(self):
        # Time Complexity: O(n)
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, data):
        # Time Complexity: O(n)
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)

    def prepend(self, data):
        # Time Complexity: O(1)
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def insert(self, data, index):
        # Time Complexity: O(n)
        if index == 0:
            self.prepend(data)
        elif self.head is None:
            raise IndexError("Index out of range")
        elif index == len(self):
            self.append(data)
        elif index > len(self):
            raise IndexError("Index out of range")
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new_node = Node(data)
            new_node.next = cur.next
            cur.next = new_node

    def delete(self, data):
        # Time Complexity: O(n)
        if self.head is None:
            raise ValueError("Data not found")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.next.data == data:
                    cur.next = cur.next.next
                    return
                cur = cur.next
            raise ValueError("Data not found")

    def pop(self):
        # Time Complexity: O(n)
        if self.head is None:
            raise ValueError("Data not found")
        elif self.head.next is None:
            self.head = None
        else:
            cur = self.head
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None

    def remove(self, index):
        # Time Complexity: O(n)
        if self.head is None:
            raise IndexError("Index out of range")
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            if cur.next is not None:
                cur.next = cur.next.next

    def getVal(self, index):
        # Time Complexity: O(n)
        if self.head is None:
            raise IndexError("Index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        if cur is None:
            raise IndexError("Index out of range")
        return cur.data

    def setVal(self, index, data):
        # Time Complexity: O(n)
        if self.head is None:
            raise IndexError("Index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        if cur is None:
            raise IndexError("Index out of range")
        cur.data = data


class DoublyLinkedList(LinkedList):
    def __init__(self, head=None):
        self.head = None
        self.tail = None

    def append(self, data):
        # Time Complexity: O(1)
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        # Time Complexity: O(1)
        new_head = Node(data)
        if self.head is not None:
            new_head.next = self.head
            self.head.prev = new_head
        self.head = new_head
        if self.tail is None:
            self.tail = new_head

    def insert(self, data, index):
        # Time Complexity: O(n)
        if index == 0:
            self.prepend(data)
        elif index == len(self):
            self.append(data)
        elif index > len(self):
            raise IndexError("Index out of range")
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new_node = Node(data)
            new_node.next = cur.next
            new_node.prev = cur
            if cur.next:
                cur.next.prev = new_node
            cur.next = new_node

    def delete(self, data):
        # Time Complexity: O(n)
        if self.head is None:
            raise ValueError("Data not found")
        elif self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        else:
            cur = self.head
            while cur is not None:
                if cur.data == data:
                    if cur.prev is not None:
                        cur.prev.next = cur.next
                    if cur.next is not None:
                        cur.next.prev = cur.prev
                    if cur == self.tail:
                        self.tail = cur.prev
                    return
                cur = cur.next
            raise ValueError("Data not found")

    def pop(self):
        # Time Complexity: O(1)
        if self.tail is None:
            raise ValueError("Data not found")
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def remove(self, index):
        # Time Complexity: O(n)
        if self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            if cur is None:
                raise IndexError("Index out of range")
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            if cur == self.tail:
                self.tail = cur.prev


if __name__ == "__main__":
    # Test LinkedList
    ll = LinkedList()
    print("Testing LinkedList")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print("LinkedList:", ll)
    ll.prepend(0)
    print("After prepend 0:", ll)
    ll.insert(6, 6)
    print("After insert 6 at index 6:", ll)
    ll.delete(6)
    print("After delete 6:", ll)
    ll.pop()
    print("After pop:", ll)
    ll.remove(2)
    print("After remove index 2:", ll)
    print("Is 3 in LinkedList?", 3 in ll)
    print("Is 6 in LinkedList?", 6 in ll)
    print("Length of LinkedList:", len(ll))
    print("Get value at index 2:", ll.getVal(2))
    ll.setVal(2, 10)
    print("After setting value at index 2 to 10:", ll)

    print("\n")

    # Test DoublyLinkedList
    dll = DoublyLinkedList()
    print("Testing DoublyLinkedList")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    print("DoublyLinkedList:", dll)
    dll.prepend(0)
    print("After prepend 0:", dll)
    dll.insert(6, 6)
    print("After insert 6 at index 6:", dll)
    dll.delete(6)
    print("After delete 6:", dll)
    dll.pop()
    print("After pop:", dll)
    dll.remove(2)
    print("After remove index 2:", dll)
    print("Is 3 in DoublyLinkedList?", 3 in dll)
    print("Is 6 in DoublyLinkedList?", 6 in dll)
    print("Length of DoublyLinkedList:", len(dll))
    print("Get value at index 2:", dll.getVal(2))
    dll.setVal(2, 10)
    print("After setting value at index 2 to 10:", dll)
