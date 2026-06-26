class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climbusingmemo(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = climbusingmemo(n-1) + climbusingmemo(n-2)
            return climbusingmemo(n-1) + climbusingmemo(n-2)
        return climbusingmemo(n)