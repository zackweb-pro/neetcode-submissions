class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_streak = 1
        current_streak = 1
        if(nums == []):
            return 0
        for c in nums:
            curr = c
            current_streak = 1
            if c -1 in set_nums:
                continue
            else:
                while curr + 1 in set_nums:
                    curr += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak