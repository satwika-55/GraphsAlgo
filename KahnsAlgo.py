'''
Kahn's algo is for finding the topo sort order of a grpah using BFS method'
'''
from collections import deque, defaultdict

def topo_sort_kahn(vertices, adj):
    # Calculate in-degrees of all vertices
    in_degree = [0] * vertices
    for i in range(vertices):
        for neighbor in adj[i]:
            in_degree[neighbor] += 1
    
    # Initialize queue and enqueue vertices with 0 in-degree
    queue = deque([i for i in range(vertices) if in_degree[i] == 0])
    
    topo_order = []
    
    # Process vertices
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        
        # Decrease in-degree for all neighbors
        for neighbor in adj[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if we were able to process all vertices (to detect cycles)
    if len(topo_order) == vertices:
        return topo_order
    else:
        return []  # Graph has a cycle, topological sorting not possible
