class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_two = 0
        prev_one = 0

        for money in nums:
            current = max(
                prev_one,          # don't rob this house
                prev_two + money   # rob this house
            )

            prev_two = prev_one
            prev_one = current

        return prev_one