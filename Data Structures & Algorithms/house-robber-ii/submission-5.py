class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums[0], self.helper(nums[0:n-1]),self.helper(nums[1:]))

    def helper(self, arr):
        rob1, rob2 = 0, 0
        for n in arr:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2