'''
4 4 5 5 6 7 7 8 9

建议一个小顶堆
始终保持堆的大小就是 n
那么堆顶元素就是第 n 大的
n = 9 时 第 n 大的数 = 1

分情况讨论
插入元素 和 堆顶元素 的关系
1、 <= 堆顶
2、  > 堆顶
因为题目中没有删除操作
所有如果一个元素 <= 堆顶元素
那么这个元素是无用的
只有当 > 堆顶元素的时候
把它插进去并且把堆顶元素删除

因为插入以后就有 n+1 个元素了
所以堆顶元素是 n+1 大的
但是我要求的是第 n 大的
第 n+1 大的以后再也不会被用到
所以直接删除
那么这个时候堆顶元素就是第 n 大的了

这里涉及到的所有操作都是 O(logn) 的

'''
###################################小(大)顶堆模板###################################
import heapq

class HeapItem:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        # 小顶堆比较元素值
        return self.val < other.val
        # 大顶堆比较元素值
        # return self.val > other.val
# heappush、heappop、heap[0]
###################################小(大)顶堆模板###################################

n, k = map(int, input().split())
heap = []

x = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(heap, HeapItem(x[i]))

x = list(map(int, input().split()))
for i in range(k):
    if x[i] > heap[0].val:
        heapq.heappush(heap, HeapItem(x[i]))
        heapq.heappop(heap)
    print(heap[0].val, end = ' ')
print()
