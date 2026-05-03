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

# ans[i] 代表 [i-k+1, i] 这个长度为 k 的区间内
# 所有元素的最小值或者最大值（可以存下标，也可以存值）
# cmpGT：  ans[i]存储的是最大值
# cmpLT:   ans[i]存储的是最小值
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

que = MonotonicQueue()

n, k = map(int, input().split())
h = [0] + list(map(int, input().split()))
ans = [0] * (n + 1)

findIntervalMinMax(que, n, k, h, ans, cmpGT)
for i in range(k, n + 1):
    print(ans[i], end=' ')
print()

findIntervalMinMax(que, n, k, h, ans, cmpLT)
for i in range(k, n + 1):
    print(ans[i], end=' ')
print()

'''
6 3
8 7 6 9 11 3
'''