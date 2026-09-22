class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if (num - 1) not in set_nums:
                n=0
                while num + n in set_nums:
                    n+=1
                longest = max(longest,n)

        return longest
        