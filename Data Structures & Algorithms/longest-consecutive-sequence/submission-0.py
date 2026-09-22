class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        seq = {}
        maxi = 0

        for num in set_nums:
            if (num - 1) in set_nums:
                continue
            elif (num - 1) not in set_nums:
                seq[num] = 1
                n = num
                while (n + 1) in set_nums:
                    seq[num] +=1
                    n+=1
        for key, value in seq.items():
            if value > maxi:
                maxi = value
        return maxi

        