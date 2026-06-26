class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtracking(start, path, total, res):
            if target == total:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i, path, nums[i]+total, res)
                path.pop()
            return res
        return backtracking(0, [], 0, [])