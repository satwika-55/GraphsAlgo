def dfs(v, visited, stack, adj):
    visited[v] = True
    # Explore all neighbors of v
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, adj)
    stack.append(v)  # Append to stack after exploring all neighbors

def topo_sort_dfs(vertices, adj):
    visited = [False] * vertices
    stack = []
    
    # Perform DFS for each unvisited vertex
    for i in range(vertices):
        if not visited[i]:
            dfs(i, visited, stack, adj)
    
    # Return the reversed stack as the topological order
    return stack[::-1]

