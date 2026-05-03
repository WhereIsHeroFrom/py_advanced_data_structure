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

class HB:
    def __init__(self):
        self.h = 0
        self.b = 0

d = Discretizer()
n, q = map(int, input().split())
hb_list = [HB() for _ in range(n)]
h_vals = list(map(int, input().split()))
for i in range(n):
    hb_list[i].h = h_vals[i]
    d.AddData(hb_list[i].h)
b_vals = list(map(int, input().split()))
for i in range(n):
    hb_list[i].b = b_vals[i]
k_list = []
for i in range(q):
    num = int(input())
    d.AddData(num)
    k_list.append(num)
d.Process()
for i in range(n):
    hb_list[i].h = d.Get(hb_list[i].h)
for i in range(q):
    k_list[i] = d.Get(k_list[i])
hb_list.sort(key=lambda x: x.h)
maxv = [-1] * (d.size + 1)
j = n - 1
for i in range(d.size - 1, -1, -1):
    maxv[i] = maxv[i + 1]
    while j >= 0 and hb_list[j].h == i:
        if hb_list[j].b > maxv[i]:
            maxv[i] = hb_list[j].b
        j -= 1
for i in range(q):
    x = k_list[i]
    print(maxv[x])
