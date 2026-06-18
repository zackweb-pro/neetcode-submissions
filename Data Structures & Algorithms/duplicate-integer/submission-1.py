class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set({})
        for a in nums:
            if a in has:
                return True
         
            has.add(a)
        return False