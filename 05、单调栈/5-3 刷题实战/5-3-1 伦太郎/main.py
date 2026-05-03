'''
学生们的视线会被不比自己身高低的人挡住
           会被 >= 自己身高的人挡住
           只要 < 自己身高，就是可以看到的
对于 h[i] 往左扫描
找到第一个 >= h[i] 的数的位置
举个例子
   i     0   1 2 3 4 5 6 7
  h[i]  inf  2 6 5 4 4 3 5

对于 h[7] 的值等于 5
而 h[3] 是第一个 >= 5 的数的位置
所以 ans[7] = 3
所以 7 号这个人能够看到的就是中间的这三个人
7号能够看到的人数 = 7 - ans[7] - 1
'''
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
findFirstMeetOnLeft(stk, n, h, ans, cmpGE)
ret = 0
for i in range(1, n + 1):
    ret += i - ans[i] - 1
print(ret)
