class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while stones:
            s1 = heapq.heappop_max(stones)
            if stones:               
                s2 = heapq.heappop_max(stones)
                if s1 != s2:
                    heapq.heappush_max(stones,s1-s2)
            else:
                return s1
        return 0