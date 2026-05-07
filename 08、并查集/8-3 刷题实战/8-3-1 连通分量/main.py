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
import sys
data = iter(sys.stdin.read().split())
n = int(next(data))
m = int(next(data))
count = n
uf = UFSet(n)

for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    if uf.Union(a, b):
        count -= 1

print(count)
