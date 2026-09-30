class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, curSum):
            nonlocal res

            if i == len(nums):
                if curSum == target:   
                    res += 1
                return

            #add 
            dfs(i + 1, curSum + nums[i])
            #subtract
            dfs(i + 1, curSum - nums[i])

        dfs(0, 0)
        return res