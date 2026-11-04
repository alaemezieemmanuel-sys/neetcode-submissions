class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxsum = nums[0]


        for num in nums:
            curSum = max(curSum,0)
            curSum +=num

            maxsum = max(maxsum, curSum)

        return maxsum
        