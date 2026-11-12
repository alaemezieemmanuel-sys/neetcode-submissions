class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for index, num in enumerate( nums):
            if index > 0 and num == nums[index -1]:
                continue
            index1 = index + 1
            index2 = len(nums) - 1
            while index1 < index2:
                sum = nums[index1] +  nums[index2] + num
                if sum == 0:
                    out.append([num, nums[index1],nums[index2]])
                    index1+=1
                    while nums[index1] == nums[index1-1] and index1< index2:
                        index1+=1
                elif sum < 0:
                    index1+=1
                else:
                    index2-=1
                    
        return out
        