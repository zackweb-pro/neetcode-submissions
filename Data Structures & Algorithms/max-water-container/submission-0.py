class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        curr_water = (r-l)*(min(heights[l], heights[r]))
        max_water = curr_water
        while l<r:
            curr_water = (r-l)*(min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
            max_water = max(max_water, curr_water)
        return max_water