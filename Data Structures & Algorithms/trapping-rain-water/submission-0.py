class Solution:
    def trap(self, height: List[int]) -> int:
        def calcmax(height):
            arr = []
            maxim = 0
            for i in range(len(height)):
                arr.append(maxim)
                if height[i] > maxim:
                    maxim = height[i]
            return arr
        leftmax = calcmax(height)
        rightmax = calcmax(height[::-1])[::-1]
        waters = [min(leftmax[i], rightmax[i]) - height[i] if min(leftmax[i], rightmax[i]) - height[i]  > 0 else 0 for i in range(len(height)) ]
        print(leftmax, rightmax, waters)
        return sum(waters)