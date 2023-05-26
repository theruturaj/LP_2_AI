# Define a class for the undirected graph
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

# DFS algorithm implementation
def dfs(graph, vertex, visited):
    # Mark the current vertex as visited and print it
    visited[vertex] = True
    print(vertex, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for i in graph[vertex]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS algorithm implementation
def bfs(graph, vertex, visited):
    # Create a queue for BFS
    queue = []

    # Mark the current vertex as visited and enqueue it
    visited[vertex] = True
    queue.append(vertex)

    while queue:
        # Dequeue a vertex from the queue and print it
        vertex = queue.pop(0)
        print(vertex, end=' ')

        # Get all adjacent vertices of the dequeued vertex. If a adjacent has not been visited,
        # then mark it visited and enqueue it
        for i in graph[vertex]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# Create an undirected graph based on user input
g = Graph()
num_edges = int(input("Enter the number of edges in the graph: "))
for i in range(num_edges):
    u, v = map(int, input("Enter the vertices of edge {}: ".format(i+1)).split())
    g.add_edge(u, v)

# DFS traversal based on user input
visited = [False] * len(g.graph)
start_vertex = int(input("Enter the starting vertex for DFS traversal: "))
print("DFS traversal:")
dfs(g.graph, start_vertex, visited)

# BFS traversal based on user input
visited = [False] * len(g.graph)
start_vertex = int(input("Enter the starting vertex for BFS traversal: "))
print("\nBFS traversal:")
bfs(g.graph, start_vertex, visited)
