class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        indexed = index + 1
        while index < len(nums):
            while indexed < len(nums):
                if nums[index] + nums[indexed] == target:
                    return [index, indexed]
                else:
                    indexed += 1
            index +=1
            indexed = index + 1