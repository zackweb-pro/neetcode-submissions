class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        longuest = 1 
        current = s[0]
        for c in s[1:]:
            current =  current+c if c not in current  else current.split(c)[1]+c
            longuest = max(longuest, len(current))
        return longuest