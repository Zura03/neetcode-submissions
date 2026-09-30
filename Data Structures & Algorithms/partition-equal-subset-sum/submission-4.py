class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) % 2

        if total != 0:
            return False

        total = sum(nums) // 2

        def dfs(i, curSum):
            if curSum == total:
                return True

            if curSum > total or i == len(nums):
                return False
                
            return (dfs(i + 1, curSum + nums[i]) or
                    dfs(i + 1, curSum))

        return dfs(0, 0)