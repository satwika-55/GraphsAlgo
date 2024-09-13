from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.transposed_graph = defaultdict(list)

    # Function to add edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Depth First Search function
    def dfs(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(node)

    # Depth First Search on the transposed graph
    def transposeDfs(self, node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in self.transposed_graph[node]:
            if not visited[neighbor]:
                self.transposeDfs(neighbor, visited, component)

    # Function to transpose the graph
    def transpose(self):
        for node in self.graph:
            for neighbor in self.graph[node]:
                self.transposed_graph[neighbor].append(node)

    # Main function to find all SCCs using Kosaraju's algorithm
    def kosaraju(self, n):
        # Step 1: Perform a DFS and fill the stack based on finishing times
        visited = [False] * n
        stack = []

        for i in range(n):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Step 2: Transpose the graph
        self.transpose()

        # Step 3: Perform DFS on the transposed graph in the order of stack
        visited = [False] * n
        scc = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                self.transposeDfs(node, visited, component)
                scc.append(component)

        return scc
