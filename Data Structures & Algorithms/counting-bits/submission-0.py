class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = list(range(0, n+1))
        return list(map(self.hammingWeight, arr))
    def hammingWeight(self, n: int) -> int:
        bi = bin(n)
        return sum(list(map(lambda x: 1 if x == '1' else 0, bi)))