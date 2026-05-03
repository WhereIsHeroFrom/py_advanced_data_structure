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

t = int(input())
for _ in range(t):
    d = Discretizer()
    n = int(input())
    a = list(map(float, input().split()))
    for num in a:
        d.AddData(num)
    d.Process()
    for num in a:
        print(d.Get(num) + 1, end=' ')
    print()
