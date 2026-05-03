'''
大顶堆维护递减序列
sum 维护堆中所有元素的和
对于模数 x 
每次弹出所有 >= x 的堆中元素
取模完毕以后再放回堆中
并且同时维护 sum 的值
当堆顶元素 < x 时结束迭代过程
'''
###################################小(大)顶堆模板###################################
import heapq

class HeapItem:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        # 小顶堆比较元素值
        # return self.val < other.val
        # 大顶堆比较元素值
        return self.val > other.val
# heappush、heappop、heap[0]
###################################小(大)顶堆模板###################################

n, k = map(int, input().split())
sum_val = 0
heap = []
x = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(heap, HeapItem(x[i]))
    sum_val += x[i]

x = list(map(int, input().split()))
for i in range(k):
    while heap and heap[0].val >= x[i]:
        sum_val -= heap[0].val
        y = heapq.heappop(heap).val % x[i]
        sum_val += y
        heapq.heappush(heap, HeapItem(y))
    print(sum_val, end=' ')
print()
