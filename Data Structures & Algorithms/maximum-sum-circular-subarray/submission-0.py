class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        CurMin = 0
        globMax =  nums[0]
        globMin = nums[0]
        total = 0


        for num in nums:
            total +=  num
            curMax += num
            CurMin += num

            curMax = max(curMax,num)

            CurMin = min(CurMin,num)
            globMax = max(globMax,curMax)
            globMin = min(globMin, CurMin)


        if globMax < 0:
            return globMax

        return max(total - globMin, globMax)
        

        
        