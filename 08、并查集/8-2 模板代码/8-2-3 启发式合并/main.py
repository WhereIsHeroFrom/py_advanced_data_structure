
####################并查集模板(启发式合并)####################
class UFSet:
    def __init__(self, n):
        self.n = n
        self.far = list(range(n + 1))
        self.height = [1] * (n + 1)
    
    def find(self, id):
        p = self.far[id]
        while p != self.far[p]:
            p = self.far[p]
        return p
    
    def Union(self, id1, id2):
        s1 = self.find(id1)
        s2 = self.find(id2) 
        if s1 == s2:
            return False
        if self.height[s1] < self.height[s2]:
            self.far[s1] = s2       
        elif self.height[s2] < self.height[s1]:
            self.far[s2] = s1
        else:
            self.far[s1] = s2
            self.height[s2] += 1
        return True
    
    def Find(self, id):
        return self.find(id)
####################并查集模板(启发式合并)####################
import sys

data = iter(sys.stdin.read().split())
n = int(next(data))
m = int(next(data))
uf = UFSet(n)

out = []
for _ in range(m):
    a = int(next(data))
    b = int(next(data))
    c = int(next(data))
    if a == 1:
        uf.Union(b, c)
    else:
        if uf.Find(b) == uf.Find(c):
            out.append("Y")
        else:
            out.append("N")

print('\n'.join(out))
