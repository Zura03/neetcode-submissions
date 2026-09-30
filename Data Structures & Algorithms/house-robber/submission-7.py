class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = nums[-1], 0
        for i in range(len(nums) - 2, -1, -1):
            temp = rob1
            rob1 = max(rob1, nums[i] + rob2)
            rob2 = temp
        return rob1