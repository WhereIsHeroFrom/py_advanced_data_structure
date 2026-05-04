#############################单调队列模板#############################

class MonotonicQueue:
    def __init__(self):
        self.data = []

# <  单调递增队列(队首->队尾)：1 2 3 4 5
def cmpLT(a, b):
    return a < b

# <= 单调不减队列(队首->队尾)：2 2 3 3 4
def cmpLE(a, b):
    return a <= b

# >  单调递减队列(队首->队尾)：6 5 4 3 2
def cmpGT(a, b):
    return a > b

# >= 单调不增队列(队首->队尾): 6 6 5 4 3
def cmpGE(a, b):
    return a >= b

# ans[i] 代表 [i-k+1, i] 中，最大值或最小值的下标
# cmpGT :  存储最大值的下标
# cmpLT :  存储最小值的下标
def findIntervalMinMax(que, n, k, h, ans, cmp):
    que.data = []
    for i in range(1, n + 1):
        while que.data and not cmp(h[que.data[-1]], h[i]):
            que.data.pop()
        que.data.append(i)
        while que.data[-1] - que.data[0] + 1 > k:
            que.data.pop(0)
        ans[i] = h[que.data[0]]

#############################单调队列模板#############################

import sys
que = MonotonicQueue()
n = int(input())
line = sys.stdin.readline()
h = list(map(int, line.split()))
h = [0] + [1e9]*n + h + [1e9]*n
k = int(input())

ans = [0] * len(h)

findIntervalMinMax(que, n*3, 2*k+1, h, ans, cmpLT)

for i in range(n+1+k, n+1+k+n):
    sys.stdout.write(str(ans[i]) + ' ')
print()