#############################单调栈模板#############################
inf = 2000000000

class MonotonicStack:
    def __init__(self):
        self.data = []

# <  单调递增栈(栈底->栈顶)：inf 1 2 3 4 5
def cmpLT(a, b):
    return a < b

# <= 单调不减栈(栈底->栈顶)：inf 2 2 3 3 4
def cmpLE(a, b):
    return a <= b

# >  单调递减栈(栈底->栈顶)：inf 6 5 4 3 2
def cmpGT(a, b):
    return a > b

# >= 单调不增栈(栈底->栈顶): inf 6 6 5 4 3
def cmpGE(a, b):
    return a >= b

# ans[i] 代表从 i 往左找，找到的第一个满足 cmp(h[x], h[i]) 的下标 x
def findFirstMeetOnLeft(stk, n, h, ans, cmp):
    h[0] = inf
    stk.data = []
    stk.data.append(0)
    for i in range(1, n + 1):
        while stk.data and not cmp(h[stk.data[-1]], h[i]):
            stk.data.pop()
        ans[i] = stk.data[-1]
        stk.data.append(i)

#############################单调栈模板#############################

stk = MonotonicStack()

n = int(input())
h = [0] + list(map(int, input().split()))
ans = [0] * (n + 1)
findFirstMeetOnLeft(stk, n, h, ans, cmpGT)
for i in range(1, n + 1):
    print(ans[i], end=' ')
print()

'''
10
2 1 4 2 1 1 3 3 2 2
0 1 0 3 4 4 3 3 8 8
'''