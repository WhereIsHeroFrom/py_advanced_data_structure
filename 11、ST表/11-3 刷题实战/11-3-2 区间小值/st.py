##########################################ST表模板##########################################
# RMQ模板
# https://www.luogu.com.cn/problem/P3865
# 静态区间最值问题

import math

class SparseTable:
    def __init__(self):
        self.org = []
        self.st = []
        self.n = 0
        self.cmp = None
    
    def Init(self, n, arr, cmp):
        self.n = n
        self.cmp = cmp
        self.org = arr.copy()
        
        # log2(n)+1, n
        log2n = int(math.log2(n)) + 1
        # st[j][i] 表示的是 [i, i + 2^j-1 ] 这个区间中的最值（所在的下标）
        # st[0][i] 表示的是 [i, i] 这个区间中的最值（所在的下标），那就是 i
        self.st = []
        self.st.append([i for i in range(n)])
        
        for j in range(1, log2n):
            if (1 << j) > n:
                break
            row = []
            for i in range(n - (1 << j) + 1):
                # [i, i+(1<<j)-1]
                '''
                    1、st[j][i] 的区间长度是 2^j
                    2、把它拆成两个长度为 2^(j-1) 的区间
                       2.1 一个区间是 [i, i + 2^(j-1) - 1]           =>  st[j-1][i]
                       2.2 一个区间是 [i + 2^(j-1), i + 2^j - 1]     =>  st[j-1][i + (1<<(j-1))]
                '''
                idx1 = self.st[j - 1][i]
                idx2 = self.st[j - 1][i + (1 << (j - 1))]
                if self.cmp(self.org[idx1], self.org[idx2]):
                    row.append(idx1)
                else:
                    row.append(idx2)
            self.st.append(row)
    
    '''
1、对于 [l, r] 这个区间，可以拆分成两个长度分别为 2^k 的区间：
    一个区间是以 l 作为起始的： [l, x]
    一个区间是以 r 作为结尾的： [y, r]
    并且，这两个区间的并集是 [l, r]， 所以需要满足 x+1 >= y
2、以 l 作为起始的区间的长度为 2 的 k 次
        它表示的区间就是 [l, l + 2^k - 1]    => x = l + 2^k - 1
   以 r 作为结尾的区间的长度为 2 的 k 次
        它表示的区间就是 [r - 2^k + 1, r]    => y = r - 2^k + 1
3、l + 2^k - 1 + 1 >= r - 2^k + 1
    移项：     2^(k+1)  >= r - l + 1
    取对数：     k      >= log2(r - l + 1) - 1
    所以 k 的值，为 log2(r - l + 1) 取上整 再减一
'''
    def Query(self, l, r):
        if l == r:
            return l
        k = math.ceil(math.log2(r - l + 1)) - 1
        idx1 = self.st[k][l]
        idx2 = self.st[k][r - (1 << k) + 1]
        if self.cmp(self.org[idx1], self.org[idx2]):
            return idx1
        else:
            return idx2
    
    def GetValue(self, idx):
        return self.org[idx]

def cmpMax(a, b):
    return a > b

def cmpMin(a, b):
    return a < b

##########################################ST表模板##########################################

st = SparseTable()
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
st.Init(n, arr, cmpMin)

for i in range(n):
    l = i - k
    r = i + k
    if l < 0:
        l = 0
    if r >= n:
        r = n - 1
    print(st.GetValue(st.Query(l, r)), end=' ')
print()
