import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        result = []
        heapq.heapify(res)
        num = k
        for point in points:
            cr  = ((point[0]**2) + (point[1]**2))
            heapq.heappush(res,[cr,point[0], point[1]])

        while num > 0:
            a = heapq.heappop(res)
            result.append([a[1], a[2]])
            num-=1

        
        return result
