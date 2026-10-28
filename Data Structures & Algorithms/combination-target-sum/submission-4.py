class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subres = []

        def dfs(i, total):
            if i == len(nums) or total > target:
                return

            if total == target:
                res.append(subres.copy())
                return

            subres.append(nums[i])
            dfs(i, total + nums[i])

            subres.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res