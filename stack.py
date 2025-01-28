class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.top = None
        self.size = 0

    def __repr__(self):
        # Time Complexity: O(n)
        cur = self.top
        res = []
        while cur is not None:
            res.append(cur.data)
            cur = cur.next
        return " → ".join(map(str, res))

    def __len__(self):
        # Time Complexity: O(1)
        return self.size

    def push(self, data):
        # Time Complexity: O(1)
        new_top = Node(data)
        new_top.next = self.top
        self.top = new_top
        self.size += 1

    def pop(self):
        # Time Complexity: O(1)
        if self.top is None:
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        # Time Complexity: O(1)
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.data

    def is_empty(self):
        # Time Complexity: O(1)
        return self.top is None


if __name__ == "__main__":
    # Test the Stack implementation
    stack = Stack()
    print("Stack type:", type(stack))
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushes:", stack)
    print("Stack length:", len(stack))
    print("Popped value:", stack.pop())
    print("Popped value:", stack.pop())
    print("Popped value:", stack.pop())
    print("Is stack empty?", stack.is_empty())
    print("Stack after popping all elements:", stack)
    print("Stack length after popping:", len(stack))
    # print(stack.pop())    # Uncomment this line to test popping from an empty stack
    print("Is stack empty?", stack.is_empty())
