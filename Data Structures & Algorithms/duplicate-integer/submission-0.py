class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = []
        for e in nums:
            if e in c:
                return True
            else:
                c.append(e)
        return False