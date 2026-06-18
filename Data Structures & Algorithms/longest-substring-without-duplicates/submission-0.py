class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set({})
        max_val = 0
        curr_val = 0
        if not(s):
            return 0
        if len(s)==1:
            return 1
        l, r = 0, 1
        hashset.add(s[l])
        while r<len(s):
            if s[r] in hashset:
                hashset.remove(s[l])
                l+=1                
            else:
                hashset.add(s[r])
                curr_val = len(hashset)
                max_val = max(curr_val, max_val)
                r+=1
        return max_val
                