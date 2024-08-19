# Disjoint Sets(Union-Find):
    # A disjoint set, also know as a union-find data structure, keeps track of a partition of a set into disjoint(non-overlapping) subsets.
    # It supports efficient union and find operations, which are essential in various algorithms, such as those for finding the connected components of a graph and Kruskal's minimum spanning tree algorithm

# Operations:
    # Find: Determines the representative(or root) of the set containing a given element. This is often used to check if two elements are in the same set.
    # Union: Merges two sets into one. This operation ensures that two elements are in the same set.

# Optimizations:
    # Path Compression: Flattens the structure of the tree whenever 'find' is called, making the trees shallower and speeding up future operations
    # Union by Rank/Size: Always attaches the smallest tree under the root of the larger tree to keep the tree balanced, reducing the height

# Applications:
    # Connected Components: Determining connected components in an undirected graph
    # Kruskals Algorithm: Finding the minimum spanning tree in a weighted graph
    # Cycle Detection: Detecting cycles in an undirected graph

# Complexity Analysis:
    # Find O(a(n)) - where a is the inverse Ackermann function, which grows very slowly, making nearly constant time
    # Union (O(n)) - similar to find operation

# Example of Disjoint Set Implementation in Python:
class DisjointSet:
        def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

        def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x]) #Path Compression
                return self.parent[x]
        
        def union(self, x, y):
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

# Example Usage
ds = DisjointSet(5)
ds.union(0, 1)
ds.union(1, 2)
print(ds.find(0))  # Output: 0
print(ds.find(1))  # Output: 0
print(ds.find(2))  # Output: 0
print(ds.find(3))  # Output: 3


# PRACTICE PROBLEMS:
# Number of Connected Components in an Undirected Graph:
    # Given 'n' nodes and a list of edges, count the number of connected components in the graph

def countComponents(n, edges):
    ds = DisjointSet(n)
    for u, v in edges:
        ds.union(u,v)
    
    root_set = set()
    for i in range(n):
         root_set.add(ds.find(i))

    return len(root_set)

# Example Usage
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(countComponents(n, edges))  # Output: 2

# Kruskal's Minimum Spanning Tree
    # Find the minimum spanning tree of a weighted graph using Kruskal's algorithm

def kruskal(n, edges):
    ds = DisjointSet(n)
    mst = []
    edges.sort(key=lambda x: x[2]) #sort edges by weight

    for u, v, weight in edges:
         if ds.find(u) != ds.find(v):
              ds.union(u,v)
              mst.append((u,v, weight))

    return mst

# Example Usage
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
print(kruskal(n, edges))  # Output: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]


