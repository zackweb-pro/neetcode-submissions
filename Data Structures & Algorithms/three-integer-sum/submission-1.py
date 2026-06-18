class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if(i==0 or nums[i]!=nums[i-1]):
                
                l, r = i+1, len(nums)-1
                while l<r:
                    if nums[i] + nums[l] + nums[r] > 0:
                        r-=1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l+=1
                    else:
                        result.append((nums[i],nums[l], nums[r]))
                        r-=1
                        l+=1
        return list(set(result))