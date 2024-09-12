class UnionFind:
  # kruskal algo - findinG MST by union By Rank
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(n, edges):
    # n is the number of vertices
    # edges is a list of tuples (weight, u, v) representing an undirected edge with a weight between u and v
    edges.sort()  # Sort edges by weight
    uf = UnionFind(n)
    mst = []  # To store the edges of the MST
    mst_weight = 0  # Total weight of the MST

    for weight, u, v in edges:
        # Check if u and v are in different components
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight
