class Solution:
    def findMin(self, nums: List[int]) -> int:
        L,R = 0, len(nums) -1
        RESULT = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                RESULT = nums[L]
                break
            M = (L +R )//2
            RESULT = min(RESULT, nums[M])
            if nums[M] >= nums[L]:
                L= M +1
            else:
                R= M

            

        return RESULT


        