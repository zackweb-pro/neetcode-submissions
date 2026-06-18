class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagrams(s, t):
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
        A = []
        B = []
        for i in range(len(strs)):
            B = []
            B.append(strs[i])
            if(sum([ strs[i] in e for e in A ])!= 0):
                continue
            for j in range(i+1, len(strs)):
                if(isAnagrams(strs[i], strs[j])):
                    B.append(strs[j])
            A.append(B)
        return A
        