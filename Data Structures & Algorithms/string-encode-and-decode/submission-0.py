class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for e in strs:
            s += e + "|*|"
        return s

    def decode(self, s: str) -> List[str]:
        L = []
        i = 0
        counter = 0
        d = ""
        while i <= len(s)-3:
            if(s[i] == "|" and s[i+1] == "*" and s[i+2] == "|"):
                counter = 1
            if(counter):
                L.append(d)
                d = ""
                counter = 0
                i+=3
                continue
            d += s[i]
            i+=1
        if(s[i:]):
            L.append(s[i:])
        return L
            