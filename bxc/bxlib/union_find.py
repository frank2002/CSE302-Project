class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        # Initialize the element if not already present.
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x

        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # Elements are already in the same set.
        if rootX == rootY:
            return

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    def replace(self, cfg):
        # Replace all occurrences of variables with their representative.
        # for i in range(len(code)):
        #     operation, *vars = code[i]
        #     new_vars = [self.find(var) for var in vars]
        #     code[i] = (operation, *new_vars)
        pass


if __name__ == "__main__":
    uf = UnionFind()
    uf.union(("L1", "%1"), "%2")
    print(uf.find("%2"))
