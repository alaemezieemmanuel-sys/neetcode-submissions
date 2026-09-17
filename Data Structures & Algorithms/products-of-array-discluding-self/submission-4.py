class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        prefix_sum=1
        suffix_sum = 1
        for i in range(0, len(nums)):
            products.append(prefix_sum)
            prefix_sum = prefix_sum * nums[i]
        for i in range(len(nums)-1,-1,-1):
            products[i] = products[i] * suffix_sum
            suffix_sum = suffix_sum * nums[i]

        return products

        