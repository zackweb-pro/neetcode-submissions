class Solution:
    def hammingWeight(self, n: int) -> int:
        bi = bin(n)
        print(bi)
        return sum(list(map(lambda x: 1 if x == '1' else 0, bi)))