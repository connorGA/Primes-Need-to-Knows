# Graphs:
    # A graph is a data structure that consists of a set of nodes(vertices) and a set of edges connecting pairs of nodes

# Types of Graphs:
    # Undirected Graph: Edges have no direction (A-B is the same as B-A)
    # Directed Graph(Digraph): Edges have a direction.(A -> B is not the same as B -> A)
    # Weighted Graph: Edges have weights or costs associated with them
    # Unweighted Graph: Edges do not have wieghts or costs

# Operations:
    # Add Vertex: Adds a vertex to the graph
    # Add Edge: Adds an edge between two vertices
    # Remove Vertex: Removes a vertex and all edges connected to it
    # Remove Edge: Removes an edge between two vertices
    # Search: FInds a path or checks the existence of a path between two vertices
    # Traversal: Visits all vertices in a specific order(e.g, BFS or DFS)

# Applications:
    # Social Networks: Representing connections between people
    # Maps and Navigation: Representing locations and routes
    # Network Topologies: Representing network connections in computer networks
    # Dependency Graphs: Representing dependencies in tasks

# Complex Analysis:
    # Add Vertex: O(1)
    # Add Edge: O(1)
    # Remove Vertex: O(V + E) where V is the number of vertices and E is the number of edges
    # Remove Edge: O(E)
    # Search (BFS/DFS): O(V + E)

# Representation:
    # Adjacency Matrix: A 2D array where the cell at row 'i' and column 'j' represents the presence (and possible the weight) of an edge berween vertices 'i' and 'j'
    # Adjacency List: An array of lists. An array index represents a vertex, and each list contains the adjacent vertices

# Example of Graph Representation:
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1) #For undirected graph
    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def bfs(self, start):
        visited = ()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.graph[vertex]) - visited)
        return visited
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited
    
# Example Usage
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
print(g.graph)  # Output: {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}

# BFS and DFS
print(g.bfs('A'))  # Output: {'A', 'B', 'C'}
print(g.dfs('A'))  # Output: {'A', 'B', 'C'}

# PRACTICE PROBLEMS:
# Graph Valid Tree:
    # Given 'n' nodes labeled from 0 to n-1 and a list of undirected edges, determine if these edges form a valid tree
def validTree(n, edges):
    if len(edges) != n-1:
        return False
    
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return False
        parent[root_u] = root_v

    return True

# Example Usage
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(validTree(n, edges))  # Output: True

# Course Schedule
    # There are a total of 'numCourses' courses you have to take, labeled from 0 to 'numCourses-1'. Some courses have prerequisites, represented as a pair '[a,b]' indicating that to take course 'a' you must first take course 'b'. Determine if you can finish all courses.

def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])

    taken_courses = 0

    while queue:
        course = queue.popleft()
        taken_courses += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return taken_courses == numCourses

# Example Usage
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))  # Output: True