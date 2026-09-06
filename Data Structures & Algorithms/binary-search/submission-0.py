class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            index = round((low+high)/2)
            number = nums[index]
            if number == target:
                return index
            elif number > target:
                high = index -1
            elif number < target:
                low = index + 1
        return -1   
        