class Node:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Indicates if this node is the end of a word


class Trie:
    def __init__(self):
        self.root = Node()

    def __repr__(self):
        # Time Complexity: O(n), where n is the total number of characters in all words
        def _repr(node, path):
            if node.is_end:
                res.append("".join(path))  # Append the current word to the result
            for char, child_node in node.children.items():
                _repr(child_node, path + [char])  # Traverse all children recursively

        res = []
        _repr(self.root, [])
        return "\n".join(res)

    def insert(self, word):
        # Time Complexity: O(m), where m is the length of the word
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()  # Add a new child node if it doesn't exist
            node = node.children[char]
        node.is_end = True  # Mark the end of the word

    def search(self, word):
        # Time Complexity: O(m), where m is the length of the word
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If a character is missing, the word doesn't exist
            node = node.children[char]
        return node.is_end  # Check if it's the end of a word

    def delete(self, word):
        # Time Complexity: O(m), where m is the length of the word
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end:
                    return False  # Word doesn't exist
                node.is_end = False  # Unmark the end of the word
                return len(node.children) == 0  # Delete the node if it's empty
            char = word[index]
            if char not in node.children:
                return False  # Word doesn't exist
            child_node = node.children[char]
            should_delete = _delete(child_node, word, index + 1)
            if should_delete:
                del node.children[char]  # Remove the child node if needed
                return len(node.children) == 0
            return False

        _delete(self.root, word, 0)

    def starts_with(self, prefix):
        # Time Complexity: O(m), where m is the length of the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # Prefix doesn't exist
            node = node.children[char]
        return True  # All characters of the prefix were found


if __name__ == "__main__":
    # Initialize the Trie
    trie = Trie()

    # Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("ap")
    trie.insert("a")
    trie.insert("banana")
    trie.insert("band")
    trie.insert("bandana")
    trie.insert("bandit")
    trie.insert("bandage")

    # Display the Trie
    print("Trie contents after insertions:")
    print(trie)
    print()

    # Test search
    print("Search for 'apple':", trie.search("apple"))  # True
    print("Search for 'banana':", trie.search("banana"))  # True
    print("Search for 'band':", trie.search("band"))  # True
    print("Search for 'bandage':", trie.search("bandage"))  # True
    print("Search for 'bandit':", trie.search("bandit"))  # True
    print("Search for 'bat':", trie.search("bat"))  # False
    print()

    # Test starts_with
    print("Starts with 'ban':", trie.starts_with("ban"))  # True
    print("Starts with 'band':", trie.starts_with("band"))  # True
    print("Starts with 'bando':", trie.starts_with("bando"))  # False
    print()

    # Test delete
    print("Deleting 'apple'...")
    trie.delete("apple")
    print("Trie contents after deleting 'apple':")
    print(trie)
    print("Search for 'apple' after deletion:", trie.search("apple"))  # False
    print()

    print("Deleting 'bandage'...")
    trie.delete("bandage")
    print("Trie contents after deleting 'bandage':")
    print(trie)
    print("Search for 'bandage' after deletion:", trie.search("bandage"))  # False
    print()

    # Final Trie state
    print("Final Trie contents:")
    print(trie)
