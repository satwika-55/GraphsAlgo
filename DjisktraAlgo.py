import heapq

def dijkstra(graph, start):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize distances with infinity
    distances = [float('inf')] * n
    distances[start] = 0  # Distance to the source is 0
    
    # Priority queue to process the nodes based on the minimum distance
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we find a greater distance in the priority queue, skip this node
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Only consider this new path if it's better than the known one
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
