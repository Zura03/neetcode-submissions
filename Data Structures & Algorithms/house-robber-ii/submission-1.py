class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def dfs(nums):
            one, two = 0, 0

            for num in nums:
                temp = two
                two = max(two, num + one)
                one = temp
            
            return two

        return max(dfs(nums[:-1]), dfs(nums[1:]))