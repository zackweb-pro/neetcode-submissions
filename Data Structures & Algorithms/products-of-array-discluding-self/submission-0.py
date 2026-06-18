class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = [1]*len(nums)
        
        for i in range(1, len(nums)):
            suffix[n-i-1]= suffix[n-i] * nums[n-i]
        products = [1]* n
        for i in range(len(nums)):
            products[i] = suffix[i]* prefix[i]
        return products