class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        cs = {}
        ct = {}
        for e in s:
            if e in cs:
                cs[e]+=1
            else: 
                cs[e] = 0
        for e in t:
            if e in ct:
                ct[e] += 1
            else:
                ct[e] = 0
        return cs == ct
