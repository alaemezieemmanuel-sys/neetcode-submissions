class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        d = deque()
        out = []
        for i, num in enumerate(nums):
            while d and num> nums[d[-1]]:
                d.pop()

            d.append(i)

            while d[0] < i-k+1:
                d.popleft()
        
            if i >= k-1:
                out.append(nums[d[0]])

        return out