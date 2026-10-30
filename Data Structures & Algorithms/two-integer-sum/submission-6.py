class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for  index, num in enumerate(nums):
            n = target - num
            if n in hashmap.keys():
                return [hashmap[n],index]
            hashmap[num] = index