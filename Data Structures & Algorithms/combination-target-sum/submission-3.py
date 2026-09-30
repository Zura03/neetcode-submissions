class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, curSum, cur):
            if curSum == target:
                res.append(cur.copy())
                return

            if curSum > target or i == len(nums):
                return

            cur.append(nums[i])
            dfs(i, curSum + nums[i], cur)
            cur.pop()

            dfs(i + 1, curSum, cur)

        dfs(0, 0, [])
        return res