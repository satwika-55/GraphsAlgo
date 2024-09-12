class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Parent of each node
        self.rank = [0] * size           # Rank (depth) of each tree
    
    def find(self, x):
        """
        Find the representative (root) of the set containing x with path compression.
        """
        if self.parent[x] != x:
            # Path compression: point the node directly to the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union the sets containing x and y using union by rank.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank: attach the smaller tree under the root of the larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                # If ranks are the same, make one root and increase its rank by 1
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
