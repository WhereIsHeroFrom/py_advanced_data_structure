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

heap = []
heapq.heappush(heap, HeapItem(5))
heapq.heappush(heap, HeapItem(2))
heapq.heappush(heap, HeapItem(8))
heapq.heappush(heap, HeapItem(1))

while heap:
    print(heap[0].val, end=' ')
    heapq.heappop(heap)
