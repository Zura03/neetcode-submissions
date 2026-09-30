class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        return dfs(0)


        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        one = nums[0]
        two = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = two
            two = max(two, one + nums[i])
            one = temp

        return two