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
sys.setrecursionlimit(1 << 16)

data = iter(sys.stdin.read().split())
n = int(next(data))
m = int(next(data))
g = Graph(n)

for _ in range(m):
    a = int(next(data)) - 1
    b = int(next(data)) - 1
    g.AddEdge(a, b, 0)

def caculate_color(u):
    visited = [False] * n
    ans = u
    
    def dfs(u):
        nonlocal ans
        if visited[u]:
            return
        visited[u] = True
        if u > ans:
            ans = u
        e = g.head[u]
        while e != -1:
            edge = g.edges[e]
            dfs(edge.to)
            e = edge.next
    
    dfs(u)
    return ans

out = []
for i in range(n):
    out.append(str(caculate_color(i) + 1))

print(' '.join(out))