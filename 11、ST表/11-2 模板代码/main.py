##########################################ST表模板##########################################
# RMQ模板
# https://www.luogu.com.cn/problem/P3865
# 静态区间最值问题
# 优化版本：IO逐行读取 + 内存严格控制 + 直接输出 + 内存优化 + log预计算

import math
import sys

class SparseTable:
    def __init__(self):
        self.st = []
        self.log_table = []
        self.cmp = None
    
    def Init(self, n, arr, cmp):
        self.cmp = cmp
        
        # log2(n)+1, n
        log2n = int(math.log2(n)) + 1
        # st[j][i] 直接存 [i, i + 2^j -1] 这个区间的最值！
        # st[0][i] 表示的是 [i, i] 这个区间的最值，那就是 arr[i]
        
        self.st = []
        self.st.append(arr.copy())  # st[0][i] 就是 arr[i]
        
        for j in range(1, log2n):
            if (1 << j) > n:
                break
            row = []
            for i in range(n - (1 << j) + 1):
                # [i, i+(1<<j)-1]
                # 1、st[j][i] 的区间长度是 2^j
                # 2、把它拆成两个长度为 2^(j-1) 的区间
                #    2.1 一个区间是 [i, i + 2^(j-1) - 1]           =>  st[j-1][i]
                #    2.2 一个区间是 [i + 2^(j-1), i + 2^j - 1]     =>  st[j-1][i + (1<<(j-1))]
                val1 = self.st[j-1][i]
                val2 = self.st[j-1][i + (1 << (j-1))]
                if self.cmp(val1, val2):
                    row.append(val1)
                else:
                    row.append(val2)
            self.st.append(row)
        
        # 预计算 log_table，log_table[i] 是 floor(log2(i))
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
    
    def Query(self, l, r):
        if l == r:
            return self.st[0][l]
        length = r - l + 1
        k = self.log_table[length]
        # 1、对于 [l, r] 这个区间，可以拆分成两个长度分别为 2^k 的区间：
        #    一个区间是以 l 作为起始的： [l, x]
        #    一个区间是以 r 作为结尾的： [y, r]
        #    并且，这两个区间的并集是 [l, r]， 所以需要满足 x+1 >= y
        # 2、以 l 作为起始的区间的长度为 2 的 k 次
        #    它表示的区间就是 [l, l + 2^k - 1]    => x = l + 2^k - 1
        #    以 r 作为结尾的区间的长度为 2 的 k 次
        #    它表示的区间就是 [r - 2^k + 1, r]    => y = r - 2^k + 1
        # 3、l + 2^k - 1 + 1 >= r - 2^k + 1
        #    移项：     2^(k+1)  >= r - l + 1
        #    取对数：     k      >= log2(r - l + 1) - 1
        #    所以 k 的值，为 log2(r - l + 1) 取上整 再减一
        val1 = self.st[k][l]
        val2 = self.st[k][r - (1 << k) + 1]
        if self.cmp(val1, val2):
            return val1
        else:
            return val2

def cmpMax(a, b):
    return a > b

def cmpMin(a, b):
    return a < b

##########################################ST表模板##########################################

def main():
    # 第一行：n, m
    line = sys.stdin.readline()
    n, m = map(int, line.strip().split())
    
    # 第二行：数组arr
    line = sys.stdin.readline()
    arr = list(map(int, line.strip().split()))
    
    st = SparseTable()
    st.Init(n, arr, cmpMax)
    
    for _ in range(m):
        line = sys.stdin.readline()
        l, r = map(int, line.strip().split())
        l -= 1
        r -= 1
        sys.stdout.write(str(st.Query(l, r)) + '\n')

if __name__ == '__main__':
    main()
