###################树状数组模板(单点更新)###################
class FenwickTree:
    def __init__(self):
        self.tree = []
        self.n = 0
    
    def lowbit(self, x):
        return x & (-x)
    
    def Init(self, n):
        self.n = n
        self.tree = [0] * (n + 2)
    
    def Update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += self.lowbit(idx)
    
    def Query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= self.lowbit(idx)
        return sum
    
    def QueryRange(self, l, r):
        return self.Query(r) - self.Query(l - 1)
###################树状数组模板(单点更新)###################
import sys

ft = FenwickTree()
line = sys.stdin.readline()
n = int(line)
line = sys.stdin.readline()
a = list(map(int, line.split()))

ft.Init(1000000)

total = 0
for i in range(n - 1, -1, -1):
    ft.Update(a[i], 1)
    total += a[i] * ft.Query(a[i] - 1)

print(total)
