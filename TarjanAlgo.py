from collections import defaultdict
'''
for finding bridges in edges
'''

class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if not vis[neighbor]:
                self.dfs(neighbor, node, vis, adj, tin, low, bridges)
                low[node] = min(low[node], low[neighbor])

                # Check if the edge is a bridge
                if low[neighbor] > tin[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], tin[neighbor])

    def criticalConnections(self, n, connections):
        adj = defaultdict(list)
        # Building the adjacency list
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []

        # We start DFS from node 0
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges
