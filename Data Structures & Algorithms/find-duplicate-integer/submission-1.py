class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        aset = set()
        for num in nums:
            if num in aset:
                return num
            else:
                aset.add(num)

        