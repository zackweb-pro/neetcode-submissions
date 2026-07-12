class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []
        def backtracking(traget, index, summ = 0):
            if summ == target:
                solution.append(traget.copy())
                traget = []
            if summ > target:
                return
            for i in range(index, len(nums)):
                traget.append(nums[i])
                backtracking(traget, i, summ+nums[i])
                traget.pop()
        backtracking([], 0, 0)
        return solution