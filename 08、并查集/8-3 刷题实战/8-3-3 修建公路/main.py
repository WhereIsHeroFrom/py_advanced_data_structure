######################Kruskal算法模板######################

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

####################并查集模板(路径压缩)####################
class UFSet:
    def __init__(self, n):
        self.n = n
        self.far = list(range(n + 1))
    
    def find(self, id):
        if self.far[id] == id:
            return id
        self.far[id] = self.find(self.far[id])
        return self.far[id] 
    
    def Union(self, id1, id2):
        s1 = self.find(id1)
        s2 = self.find(id2)
        if s1 == s2:
            return False
        self.far[s1] = s2
        return True
    
    def Find(self, id):
        return self.find(id)
####################并查集模板(路径压缩)####################
######################Kruskal算法模板######################

import sys

data = iter(sys.stdin.read().split())   
n = int(next(data))
m = int(next(data))

edges = []
for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))
    edges.append(Edge(a, b, c))

edges.sort(key=lambda e: e.w)
uf = UFSet(n)
total = 0
cnt = 0

for e in edges:
    if uf.Union(e.u, e.v):
        total += e.w
        cnt += 1
        if cnt == n - 1:
            break

if cnt != n - 1:
    print("-1")
else:
    print(total)
