############################ST表模板############################
import math

def cmpMax(a, b):
    return a > b

def cmpMin(a, b):
    return a < b

class SparseTable:
    def __init__(self):
        self.org = []
        self.st = []
        self.n = 0
        self.cmp = None
        self.log_table = []

    def Init(self, n, arr, cmp):
        self.n = n
        self.cmp = cmp
        self.org = arr.copy()

        log2n = int(math.log2(n)) + 1
        # st[j][i] 表示的是 [i, i+2^j-1] 这个区间的最值所在下标
        # st[0][i] 表示的是 [i, i] 这个区间的最值所在下标
        self.st = []
        self.st.append( [i for i in range(n)] )

        for j in range(1, log2n):
            if (1<<j) > n:
                break
            row = []
            # i < n - (1<<j) + 1
            # i + (1<<j) - 1 < n
            for i in range(n - (1<<j) + 1):
                # [i, i + (1<<j) - 1]
                '''
                1、st[j][i] 的区间长度是 2^j
                2、把它拆成两个长度为 2^(j-1) 的区间
                    2.1 [i, i + 2^(j-1) - 1]
                    2.2 [i + 2^(j-1), i + 2^j - 1]
                '''
                idx1 = self.st[j-1][i]
                idx2 = self.st[j-1][i + (1<<(j-1))]
                if self.cmp(self.org[idx1], self.org[idx2]):
                    row.append(idx1)
                else:
                    row.append(idx2)
                    
            self.st.append(row)  
            
        self.log_table = [0] * (n+1)
        for i in range(2, n+1):
            self.log_table[i] = self.log_table[i//2] + 1

    '''
     1、对于区间 [l, r]，可以拆分成两个长度分别为 2^k 的区间
         一个区间是以 l 作为起始：[l, x]
         一个区间是以 r 作为结尾：[y, r]
         并且这两个区间的并集是[l, r]，所以需要满足 x+1 >= y
     2、以 l 作为起始的区间长度为 2 的 k 次
         [l, l + 2^k - 1]  -> x = l + 2^k - 1
        以 r 作为结尾的区间长度为 2 的 k 次
         [r - 2^k + 1, r]  -> y = r - 2^k + 1
     3、l + 2^k - 1 + 1 >= r - 2^k + 1
     移项：      2^(k+1) >= r - l + 1
     取对数：      k+1    >=  log2(r - l + 1)
     移项：        k      >= log2(r - l + 1) - 1
    '''
    def Query(self, l, r) :
        if l == r:
            return l
        k = self.log_table[r - l + 1]
        idx1 = self.st[k][l]
        idx2 = self.st[k][r - (1<<k) + 1]
        if self.cmp(self.org[idx1], self.org[idx2] ):
            return idx1
        return idx2

    def GetValue(self, idx):
        return self.org[idx]

############################ST表模板############################

import sys

st = SparseTable()
n, k = map(int, input().split())

line = sys.stdin.readline()
arr = list(map(int, line.split()))

st.Init(n, arr, cmpMax)

while k > 0:
    line = sys.stdin.readline()
    l, r = map(int, line.split())
    l -= 1
    r -= 1
    idx = st.Query(l, r)
    ans = st.GetValue(idx)
    sys.stdout.write(str(ans) + '\n')
    k -= 1
