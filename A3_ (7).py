import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_distance(self, dist, spt_set):
        min_value = sys.maxsize
        min_index = None
        for v in range(self.V):
            if dist[v] < min_value and spt_set[v] is False:
                min_value = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        spt_set = [False] * self.V
        dist[src] = 0

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if (
                    not spt_set[v]
                    and self.graph[u][v] > 0
                    and dist[u] + self.graph[u][v] < dist[v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

# Get user input for the number of vertices
num_vertices = int(input("Enter the number of vertices in the graph: "))

# Create a Graph object
g = Graph(num_vertices)

# Get user input for edges and weights
num_edges = int(input("Enter the number of edges in the graph: "))
print("Enter the source, destination, and weight for each edge:")

for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    g.add_edge(u, v, weight)

# Get user input for the source vertex
src = int(input("Enter the source vertex: "))

# Perform Dijkstra's algorithm
distances = g.dijkstra(src)

# Print the shortest distances
print("Shortest distances from source vertex", src, "to all other vertices:")
for v in range(g.V):
    print("Vertex", v, "-> Distance:", distances[v])
