########################链式前向星模板########################
class Edge:
    def __init__(self, to, weight, next_edge):
        self.to = to
        self.weight = weight
        self.next = next_edge

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.head = [-1] * n
        self.edge_count = 0
    
    def AddEdge(self, from_node, to_node, weight=0):
        self.edges.append(Edge(to_node, weight, self.head[from_node]))
        self.head[from_node] = self.edge_count
        self.edge_count += 1
    
    def PrintEdges(self):
        for i in range(self.n):
            print(f"{i}:", end="")
            e = self.head[i]
            while e != -1:
                edge = g.edges[e]
                print(f"({edge.to},{edge.weight})", end="")
                e = edge.next
            print()
########################链式前向星模板########################

import sys

data = iter(sys.stdin.read().split())
n = int(next(data))
m = int(next(data))
g = Graph(n)
for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))
    g.AddEdge(a, b, c)
g.PrintEdges()