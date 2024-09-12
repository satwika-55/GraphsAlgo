class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Parent of each node
        self.size = [1] * size           # Size of each set (initially 1 for all)

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
        Union the sets containing x and y using union by size.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size: attach the smaller tree under the root of the larger tree
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

