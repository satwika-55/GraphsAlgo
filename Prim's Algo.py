import heapq
def prim_mst(graph):
    """
    Function to find the Minimum Spanning Tree (MST) of a graph using Prim's algorithm.
    
    :param graph: Dictionary representation of the graph where graph[u] = [(v, weight), ...]
                  means there's an edge from vertex u to vertex v with the given weight.
    :return: A list of edges in the MST and the total weight of the MST.
    """
    # Initialize variables
    mst_edges = []  # To store the edges in the MST
    visited = set()  # To keep track of visited nodes
    min_heap = []  # Priority queue to select the minimum weight edge
    total_weight = 0  # Total weight of the MST

    # Start with an arbitrary node, here node '0'
    start_node = 0
    visited.add(start_node)
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    # While there are edges to process in the heap
    while min_heap:
        # Get the edge with the smallest weight
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue

        # Add the edge to the MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        # Add the edges connected to the newly visited node
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return mst_edges, total_weight
