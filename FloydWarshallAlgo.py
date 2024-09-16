class Solution:
    def floydWarshall(self, graph: List[List[int]]) -> List[List[int]]:
        # Number of vertices in the graph
        n = len(graph)
        
        # Initialize the distance matrix with the input graph
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Fill in the initial distances
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0  # Distance to self is 0
                elif graph[i][j] != -1:  # If there's an edge, set the distance to the edge weight
                    dist[i][j] = graph[i][j]
        
        # Main Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update the shortest path from i to j through vertex k
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Check for negative cycles
        for i in range(n):
            if dist[i][i] < 0:
                print("Graph contains a negative weight cycle")
                return []

        # Return the distance matrix
        return dist

