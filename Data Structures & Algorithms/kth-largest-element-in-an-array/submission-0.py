import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        while k:
            g = heapq.heappop_max(nums)
            k-=1

        return g
        