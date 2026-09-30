class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        R = 0
        curSum = 0
        res = nums[0]
        while R < len(nums):
            curSum += nums[R]
            R += 1
            res = max(curSum, res)

            if curSum < 0:
                curSum = 0
        return res