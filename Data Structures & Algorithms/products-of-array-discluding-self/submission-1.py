class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1]*len(nums)
        for i in range(1, len(nums)):
            products[i] = products[i-1] * nums[i-1]
        post = 1
        for i in range(0, len(nums)):
            products[n-1-i] *= post
            post*=nums[n-i-1]
        return products