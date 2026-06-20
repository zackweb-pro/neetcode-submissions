class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = nums[l]
        while l <= r:
            if nums[l]< nums[r]:
                minimum = min(nums[l], minimum)
                break
            m = (r+l)//2
            minimum = min(minimum, nums[m])
            print(l, r, m)

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return minimum