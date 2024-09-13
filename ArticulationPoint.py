from collections import defaultdict

class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if not vis[neighbor]:
                self.dfs(neighbor, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[neighbor])

                # Check articulation point condition
                if low[neighbor] >= tin[node] and parent != -1:
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node], tin[neighbor])

        # Special case for root node
        if child > 1 and parent == -1:
            mark[node] = 1

    def articulationPoints(self, n, adj):
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        mark = [0] * n

        for i in range(n):
            if not vis[i]:
                self.dfs(i, -1, vis, tin, low, mark, adj)

        ans = [i for i in range(n) if mark[i] == 1]

        if not ans:
            ans.append(-1)
        return ans

