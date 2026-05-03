'''
首先看到求最大的数，我们首先想到大顶堆
那么假设有一个堆 heap
往堆里面不断的压入元素
heap : 6 7 4 2 1 5 7
如果没有加减的操作
那么每次弹出的堆顶元素就是最大值
但是要把堆中的元素都加上x或者减去x
这个操作对于堆来说是不支持的
所以可以采用一个额外的变量 sum
所有的加减操作都在这个sum上进行
比如堆中按顺序压入
5 6 7 3 2 
然后突然进行了一些加减
+x -y +z -w
这些元素的和我们可以用 sum 来表示
你就可以想象成这个sum累加到了堆中元素的每一项上
但是实际上并没有加上
因为堆不支持这个操作
但是当我弹出一个堆顶元素的时候
实际的值就是 堆顶元素 + sum
这样一来 2 3 4 的操作的时间复杂度
就都是 O(1) 的了
再来看第一个操作
如果目前 sum 不等于 0
然后我往堆里当了一个元素 x
弹出的时候结果是 x + sum
你会发现 压入 和 弹出 的值
不匹配
多了 sum 这部分
原因是这个sum是在压入元素之前累加上的
x 本身并没有享受到这个 sum 的加成
所以只有在压入 x 以后产生的 sum
才需要在弹出的时候累加上
那我们是否需要多个 sum 呢？
不需要
我只要在进入堆之间
把实际要压入的元素变成 x - sum
这样弹出的时候就是 x - sum + sum
得到的就是原值
这样操作1也变成 O(1) 了
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
heapq.heappush(heap, HeapItem(k))

for _ in range(n):
    a, *args = map(int, input().split())
    if a == 4:
        print(heap[0].val + sum_val)
        heapq.heappop(heap)
    else:
        x = args[0]
        if a == 1:
            heapq.heappush(heap, HeapItem(x - sum_val))
        elif a == 2:
            sum_val += x
        elif a == 3:
            sum_val -= x
