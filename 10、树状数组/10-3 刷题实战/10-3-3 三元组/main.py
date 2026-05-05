mod = 998244353

###########################离散化模板###########################
# https://www.luogu.com.cn/problem/B3694

# 2333 20 1.7 -5 20 1 20 -5
# 第一步：排序  -5 -5 1 1.7 20 20 20 2333
# 第二步：去重  -5 1 1.7 20 2333
#               0  1 2   3  4

class Discretizer:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def AddData(self, v):
        self.data.append(v)
        self.size += 1
    
    def Process(self):
        self.data.sort()
        last_idx = 0
        for i in range(1, self.size):
            x = self.data[i]
            if x != self.data[last_idx]:
                last_idx += 1
                self.data[last_idx] = x
        self.size = last_idx + 1
        self.data = self.data[:self.size]  # 截断
    
    def Get(self, v):
        l = -1
        r = self.size
        while l + 1 < r:
            mid = (l + r) >> 1
            if self.data[mid] >= v:
                r = mid
            else:
                l = mid
        if r == self.size or self.data[r] != v:
            return -1
        return r
###########################离散化模板###########################

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

d = Discretizer()
ft = FenwickTree()

line = sys.stdin.readline()
n = int(line)

a = []
line = sys.stdin.readline()
vals = list(map(int, line.split()))
for i in range(n):
    val = vals[i]
    a.append(val)
    d.AddData(val)

d.Process()
for i in range(n):
    a[i] = d.Get(a[i]) + 1

ft.Init(n)
lt = [0] * n

for i in range(n):
    ft.Update(a[i], 1)
    lt[i] = ft.Query(a[i] - 1)

ft.Init(n)

total = 0
for i in range(n - 1, -1, -1):
    ft.Update(a[i], 1)
    gt = ft.QueryRange(a[i] + 1, n)
    total = (total + lt[i] * gt) % mod

print(total)
