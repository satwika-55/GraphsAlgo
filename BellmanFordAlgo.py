class Solution:
    def bellmanFord(self, n: int, edges: List[List[int]], src: int) -> List[int]:
        # Step 1: Initialize distances
        dist = [float('inf')] * n
        dist[src] = 0

        # Step 2: Relax all edges (n - 1) times
        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Step 3: Check for negative-weight cycles
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return []

        # Return the shortest distances
        return dist
