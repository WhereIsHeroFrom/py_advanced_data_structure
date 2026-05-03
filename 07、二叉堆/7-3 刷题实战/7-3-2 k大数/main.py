'''
1 2 3 4 5 6 7 8 9

建立一个小顶堆
并且始终保持堆的大小是 n
那么堆顶元素就是第 n 大的
n=9 第n大的数 = 1

分情况讨论
插入的元素比堆顶的元素的关系
1、<= 堆顶
2、>  堆顶
因为没有删除操作
所以如果一个元素 <= 堆顶元素
那么根本不需要插入堆中
会破坏原有堆的性质
因为要保证堆的元素始终是 n 个
只有当 > 堆顶元素的时候
把它插进去并且把堆顶元素删除
因为现在是 n+1 个元素
所以堆顶是第 n+1 大的那个
而这个元素以后再也不会被用到
所以直接删除
那么这时候堆顶的元素就是第 n 大的
所有操作都是 O(1) 的
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
    print(heap[0].val, end=' ')
print()
