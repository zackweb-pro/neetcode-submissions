class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for e in nums: 
            if e in c:
                c[e] += 1
            else:
                c[e] = 0
        cf = [key for key, val in sorted(c.items(), key=lambda item: item[1])]
        cf.reverse()
        return cf[:k]