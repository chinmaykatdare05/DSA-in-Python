from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        # Time Complexity: O(n)
        res = []
        self.in_order(self.root, res)
        return " → ".join(map(str, res))

    def __len__(self):
        # Time Complexity: O(n)
        res = []
        self.in_order(self.root, res)
        return len(res)

    def __contains__(self, data):
        # Time Complexity: O(h), where h is the height of the tree
        return self.search(data) is not None

    def search(self, data):
        # Time Complexity: O(h)
        cur = self.root
        while cur is not None:
            if data == cur.data:
                return cur
            elif data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def insert(self, data):
        # Time Complexity: O(h)
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left is None:
                        cur.left = new_node
                        new_node.parent = cur
                        break
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = new_node
                        new_node.parent = cur
                        break
                    cur = cur.right

    def delete(self, data):
        # Time Complexity: O(h)
        node = self.search(data)
        if node is None:
            raise ValueError("Node not found")
        if node.left is None and node.right is None:
            # Case 1: Node is a leaf
            if node.parent is None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is None:
            # Case 2: Node has only a right child
            if node.parent is None:
                self.root = node.right
            elif node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent
        elif node.right is None:
            # Case 3: Node has only a left child
            if node.parent is None:
                self.root = node.left
            elif node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent
        else:
            # Case 4: Node has two children
            successor = self.get_min(node.right)
            node.data = successor.data
            if successor.parent.left == successor:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            if successor.right is not None:
                successor.right.parent = successor.parent

    def get_min(self, node):
        # Time Complexity: O(h)
        while node.left is not None:
            node = node.left
        return node

    def in_order(self, node, res):
        # Time Complexity: O(n)
        if node is not None:
            self.in_order(node.left, res)
            res.append(node.data)
            self.in_order(node.right, res)

    def pre_order(self, node, res):
        # Time Complexity: O(n)
        if node is not None:
            res.append(node.data)
            self.pre_order(node.left, res)
            self.pre_order(node.right, res)

    def post_order(self, node, res):
        # Time Complexity: O(n)
        if node is not None:
            self.post_order(node.left, res)
            self.post_order(node.right, res)
            res.append(node.data)

    def height(self, node):
        # Time Complexity: O(n)
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self):
        # Time Complexity: O(n)
        if self.root is None:
            return True
        return abs(self.height(self.root.left) - self.height(self.root.right)) <= 1

    def is_full(self):
        # Time Complexity: O(n)
        if self.root is None:
            return True
        return self._is_full(self.root)

    def _is_full(self, node):
        # Time Complexity: O(n)
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full(node.left) and self._is_full(node.right)
        return False

    def is_perfect(self):
        # Time Complexity: O(n)
        if self.root is None:
            return True
        return self._is_perfect(self.root)

    def _is_perfect(self, node):
        # Time Complexity: O(n)
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_perfect(node.left) and self._is_perfect(node.right)
        return False

    def is_complete(self):
        # Time Complexity: O(n)
        if self.root is None:
            return True
        q = Queue()
        q.put(self.root)
        flag = False
        while not q.empty():
            node = q.get()
            if flag and (node.left is not None or node.right is not None):
                return False
            if node.left is None and node.right is not None:
                return False
            if node.left is not None:
                q.put(node.left)
            else:
                flag = True
            if node.right is not None:
                q.put(node.right)
            else:
                flag = True
        return True

    def is_bst(self):
        # Time Complexity: O(n)
        return self._is_bst(self.root, float("-inf"), float("inf"))

    def _is_bst(self, node, min_val, max_val):
        # Time Complexity: O(n)
        if node is None:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False
        return self._is_bst(node.left, min_val, node.data) and self._is_bst(
            node.right, node.data, max_val
        )


if __name__ == "__main__":
    # Initialize BST and insert nodes
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(17)

    # Printing the BST
    print("BST (In-order):", bst)

    # Test height
    print("Height of BST:", bst.height(bst.root))

    # Test search
    print("Search 7:", bst.search(7) is not None)
    print("Search 20:", bst.search(20) is not None)

    # Test __contains__ (operator in)
    print("Is 7 in BST?", 7 in bst)
    print("Is 20 in BST?", 20 in bst)

    # Test __len__
    print("Number of nodes in BST (len):", len(bst))

    # Test is_balanced
    print("Is BST balanced?", bst.is_balanced())

    # Test is_full
    print("Is BST full?", bst.is_full())

    # Test is_perfect
    print("Is BST perfect?", bst.is_perfect())

    # Test is_complete
    print("Is BST complete?", bst.is_complete())

    # Test is_bst
    print("Is BST valid?", bst.is_bst())

    # Test traversals
    in_order_res = []
    pre_order_res = []
    post_order_res = []
    bst.in_order(bst.root, in_order_res)
    bst.pre_order(bst.root, pre_order_res)
    bst.post_order(bst.root, post_order_res)

    print("In-order traversal:", in_order_res)
    print("Pre-order traversal:", pre_order_res)
    print("Post-order traversal:", post_order_res)

    # Test delete
    bst.delete(7)  # Delete a node with no children
    print("BST after deleting 7:", bst)
    bst.delete(5)  # Delete a node with one child
    print("BST after deleting 5:", bst)
    bst.delete(10)  # Delete the root node
    print("BST after deleting root (10):", bst)

    # Test is_degenerate
    print("Is BST degenerate?", bst.is_degenerate())

    # Test symmetry
    print("Is BST symmetric?", bst.is_symmetric())

    # Test mirror (by creating a mirror tree)
    mirror_bst = BinarySearchTree()
    mirror_bst.insert(10)
    mirror_bst.insert(15)
    mirror_bst.insert(5)
    mirror_bst.insert(17)
    mirror_bst.insert(12)
    mirror_bst.insert(7)
    mirror_bst.insert(3)

    print("Is BST a mirror of another BST?", bst.is_mirror(mirror_bst))

    # Test subtree
    subtree = BinarySearchTree()
    subtree.insert(12)
    subtree.insert(17)
    print("Is subtree:", bst.is_subtree(subtree))

    # Final BST state
    print("Final BST (In-order):", bst)
    print("Final BST length:", len(bst))
