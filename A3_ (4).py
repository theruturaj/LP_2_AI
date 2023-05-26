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
        self.graph[v][u] = weight

# Example usage:
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

src = 0
distances = g.dijkstra(src)

print("Shortest distances from source vertex", src, "to all other vertices:")
for v in range(g.V):
    print("Vertex", v, "-> Distance:", distances[v])
