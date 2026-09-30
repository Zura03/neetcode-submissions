class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, curSum):
            if i == len(nums):
                if curSum == target:   
                    return 1
                return 0

            dp[(i, curSum)] = (dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i]))
            return dp[(i, curSum)]

        return dfs(0, 0)
