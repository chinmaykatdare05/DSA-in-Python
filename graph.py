class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def __repr__(self):
        res = []
        for node, neighbors in self.adjacency_list.items():
            res.append(f"{node} → {neighbors}")
        return "\n".join(res)

    def __len__(self):
        return len(self.adjacency_list)

    def __contains__(self, node):
        return node in self.adjacency_list

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        self.adjacency_list[node1].append(node2)
        if not self.directed:
            self.adjacency_list[node2].append(node1)

    def remove_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for neighbors in self.adjacency_list.values():
                if node in neighbors:
                    neighbors.remove(node)

    def remove_edge(self, node1, node2):
        if node1 in self.adjacency_list:
            if node2 in self.adjacency_list[node1]:
                self.adjacency_list[node1].remove(node2)
        if node2 in self.adjacency_list:
            if node1 in self.adjacency_list[node2]:
                self.adjacency_list[node2].remove(node1)

    def has_node(self, node):
        return node in self.adjacency_list

    def has_edge(self, node1, node2):
        return node2 in self.adjacency_list.get(node1, [])

    def is_adjacent(self, node1, node2):
        return node2 in self.adjacency_list.get(node1, [])

    def neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def depth_first_search(self, start):
        visited = set()

        def _dfs(node):
            visited.add(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return visited

    def breadth_first_search(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            visited.add(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return visited

    def shortest_path(self, start, end):
        queue = [(start, [start])]
        while queue:
            node, path = queue.pop(0)
            for neighbor in self.adjacency_list[node]:
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))
        return None

    def dijkstra(self, start):
        distances = {node: float("inf") for node in self.adjacency_list}
        distances[start] = 0
        queue = [start]
        while queue:
            node = queue.pop(0)
            for neighbor in self.adjacency_list[node]:
                new_distance = distances[node] + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    queue.append(neighbor)
        return distances

    def topological_sort(self):
        visited = set()
        stack = []

        def _topological_sort(node):
            visited.add(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    _topological_sort(neighbor)
            stack.append(node)

        for node in self.adjacency_list:
            if node not in visited:
                _topological_sort(node)
        return stack[::-1]

    def is_cyclic(self):
        visited = set()
        stack = set()

        def _is_cyclic(node):
            visited.add(node)
            stack.add(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    if _is_cyclic(neighbor):
                        return True
                elif neighbor in stack:
                    return True
            stack.remove(node)
            return False

        for node in self.adjacency_list:
            if node not in visited:
                if _is_cyclic(node):
                    return True
        return False

    def connected_components(self):
        visited = set()
        components = []

        def _connected_components(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    _connected_components(neighbor, component)

        for node in self.adjacency_list:
            if node not in visited:
                component = []
                _connected_components(node, component)
                components.append(component)
        return components

    def minimum_spanning_tree(self):
        mst = Graph()
        if not self.adjacency_list:
            return mst
        start = next(iter(self.adjacency_list))
        visited = set()
        queue = [(start, None)]
        while queue:
            node, parent = queue.pop(0)
            visited.add(node)
            if parent is not None:
                mst.add_edge(parent, node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    queue.append((neighbor, node))
        return mst

    def to_adjacency_matrix(self):
        nodes = list(self.adjacency_list)
        matrix = [[0] * len(nodes) for _ in range(len(nodes))]
        node_to_index = {node: i for i, node in enumerate(nodes)}
        for node, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                matrix[node_to_index[node]][node_to_index[neighbor]] = 1
        return matrix


if __name__ == "__main__":
    # Initialize a directed graph
    g = Graph(directed=True)
    print("Graph initialized:", type(g))

    # Add nodes and edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "A")
    g.add_edge("C", "D")
    g.add_edge("D", "D")

    # Display the graph
    print("\nGraph representation:")
    print(g)

    # Basic operations
    print("\nGraph size (number of nodes):", len(g))
    print("Is 'A' in the graph?", "A" in g)
    print("Is 'E' in the graph?", "E" in g)
    print("Does graph have node 'A'?", g.has_node("A"))
    print("Does graph have edge 'A' -> 'B'?", g.has_edge("A", "B"))
    print("Does graph have edge 'B' -> 'A'?", g.has_edge("B", "A"))
    print("Neighbors of 'A':", g.neighbors("A"))

    # Traversal
    print("\nDepth First Search (starting at 'A'):", g.depth_first_search("A"))
    print("Breadth First Search (starting at 'A'):", g.breadth_first_search("A"))

    # Pathfinding
    print("\nShortest path from 'A' to 'D':", g.shortest_path("A", "D"))
    print("Dijkstra's shortest path distances from 'A':", g.dijkstra("A"))

    # Graph properties
    print("\nTopological Sort:", g.topological_sort())
    print("Is the graph cyclic?", g.is_cyclic())
    print("Connected components:", g.connected_components())

    # Minimum Spanning Tree
    print("\nMinimum Spanning Tree:")
    print(g.minimum_spanning_tree())

    # Adjacency matrix
    print("\nAdjacency Matrix:")
    matrix = g.to_adjacency_matrix()
    for row in matrix:
        print(row)

    # Modifications (remove nodes and edges)
    print("\nRemoving node 'D'...")
    g.remove_node("D")
    print("Graph after removing 'D':")
    print(g)

    print("\nRemoving edge 'A' -> 'B'...")
    g.remove_edge("A", "B")
    print("Graph after removing edge 'A' -> 'B':")
    print(g)

    # Add nodes and edges again for testing cyclic behavior
    print("\nRe-adding edges and nodes:")
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    print(g)

    # Final tests
    print("\nFinal Graph state:")
    print("Is the graph cyclic?", g.is_cyclic())
    print("Connected components:", g.connected_components())
    print("Minimum Spanning Tree:", g.minimum_spanning_tree())
