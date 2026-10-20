import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify_max(self.nums)

    def add(self, val: int) -> int:
        l = []
        heapq.heappush_max(self.nums, val)
        num  = self.k
        while num > 0:
            a = heapq.heappop_max(self.nums)
            l.append(a)
            num-=1

        for i in l:
            heapq.heappush_max(self.nums,i)

        return l[-1]
        
