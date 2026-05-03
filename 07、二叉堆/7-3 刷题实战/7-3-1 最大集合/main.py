'''
首先看到求最大的数，我们首先想到的是大顶堆
那么假设有一个堆 heap
往对立面不断的压入元素
heap: 6 7 4 2 1 5 7
如果没有加减的操作
那么每次弹出的堆顶元素就是最大值
但是要把堆中的元素都加上 x 或者 -x
这个操作对于堆来说是不支持的

所以可以采用一个额外的变量 sum
所有的加减操作都在 sum 上进行
比如堆中按顺序压入 
5 6 7 3 2
然后突然进行了一些加减操作
+x  -y   +z   -w
这些元素的和我们可以用 sum 来表示
你就可以想象成这个 sum 累加到了堆中每一个元素上
（但是实际上并没有加上，因为堆不支持所有元素操作）
但是当我弹出一个堆顶元素的时候
实际的值应该是 堆顶元素 + sum

这样一来，2 、3 、4 三个操作
时间复杂度就变成了 O(logn)

再来看第 1 个操作
如果目前 sum 不等于 0
然后我往堆里插入一个元素 x
弹出的时候结果变成了 x + sum
你会发现压入和弹出的值不匹配
多了 sum 这部分

原因：
sum 是压入元素之前累加上的
x 本身并没有享受到这个sum的加成
所以只有在压入 x 以后产生的sum
才需要在弹出的时候加上

那我们是否需要多个 sum 呢？？？？
不需要
只需要在这个元素 x 进入对之前
把它变成 x - sum 就可以了
这样弹出的时候就是 x-sum + sum = x
这样操作 1 也变成 O(logn)

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
        else:
            sum_val -= x
