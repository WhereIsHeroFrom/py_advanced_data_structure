##########################线段树模板(区间求和)##########################
class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.tree = [0] * (n * 4)
        self.lazy = [0] * (n * 4)
        self.build(0, 0, n-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return 
        mid = (start + end) // 2
        left_child = node*2 + 1
        right_child = left_child + 1
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def pushDown(self, node, start, end):
        if self.lazy[node] != 0:
            mid = (start + end) // 2
            left_child = node*2 + 1
            right_child = left_child + 1
            self.tree[left_child] += self.lazy[node] * (mid - start + 1)
            self.tree[right_child] += self.lazy[node] * (end - mid)

            self.lazy[left_child] += self.lazy[node]
            self.lazy[right_child] +=  self.lazy[node]

            self.lazy[node] = 0
    
    def updateRange(self, node, start, end, l, r, val):
        if start > r or end < l:
            return 
        # l    start   end    r
        if start >= l and end <= r:
            self.tree[node] += val * (end - start + 1)
            self.lazy[node] += val
            return 
        self.pushDown(node, start, end)
        mid = (start + end) // 2
        left_child = node*2 + 1
        right_child = left_child + 1
        self.updateRange(left_child, start, mid, l, r, val)
        self.updateRange(right_child, mid+1, end, l, r, val)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def queryRange(self, node, start, end, l, r):
        if start > r or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[node]
        self.pushDown(node, start, end)
        mid = (start + end) // 2
        left_child = node*2 + 1
        right_child = left_child + 1
        lsum = self.queryRange(left_child, start, mid, l, r)
        rsum = self.queryRange(right_child, mid+1, end, l, r)
        return lsum + rsum
    
    def Update(self, l, r, val):
        self.updateRange(0, 0, n-1, l, r, val)

    def Query(self, l, r):
        return self.queryRange(0, 0, n-1, l, r)

##########################线段树模板(区间求和)##########################

n = int(input())
a = list(map(int, input().split()))
m = int(input())
seg = SegmentTree(n, a)
while m > 0:
    z, x, y = map(int, input().split())
    x -= 1
    if z == 1:
        seg.Update(x, x, y)
    else:
        y -= 1
        print(seg.Query(x, y))
    m -= 1
