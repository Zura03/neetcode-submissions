class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, numbers):
        if not numbers:
            return 0
        rob1, rob2 = numbers[-1], 0
        for i in range(len(numbers) - 2, -1, -1):
            temp = rob1
            rob1 = max(rob1, numbers[i] + rob2)
            rob2 = temp
        return rob1