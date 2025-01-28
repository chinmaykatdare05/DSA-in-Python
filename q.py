class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.front = None
        self.rear = None
        self.size = 0

    def __repr__(self):
        # Time Complexity: O(n)
        cur = self.front
        res = []
        while cur is not None:
            res.append(cur.data)
            cur = cur.next
        return " → ".join(map(str, res))

    def __len__(self):
        # Time Complexity: O(1)
        return self.size

    def enqueue(self, data):
        # Time Complexity: O(1)
        new_rear = Node(data)
        if self.front is None:
            # If queue is empty, set both front and rear to the new node
            self.front = new_rear
            self.rear = new_rear
        else:
            # Link the new node to the rear and update rear
            self.rear.next = new_rear
            self.rear = new_rear
        self.size += 1

    def dequeue(self):
        # Time Complexity: O(1)
        if self.front is None:
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            # If the queue becomes empty, reset rear as well
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        # Time Complexity: O(1)
        if self.front is None:
            raise IndexError("Queue is empty")
        return self.front.data

    def is_empty(self):
        # Time Complexity: O(1)
        return self.front is None


if __name__ == "__main__":
    # Test the Queue implementation
    q = Queue()
    print("Queue type:", type(q))
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue after enqueues:", q)
    print("Queue length:", len(q))
    print("Dequeued value:", q.dequeue())
    print("Front value after dequeue (peek):", q.peek())
    print("Dequeued value:", q.dequeue())
    print("Dequeued value:", q.dequeue())
    print("Is queue empty?", q.is_empty())
    print("Queue length after all dequeues:", len(q))
    print("Queue after all dequeues:", q)
    # print(q.dequeue())    # Uncomment this line to test dequeueing from an empty queue
