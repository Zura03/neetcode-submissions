class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1, 1

        for num in nums:
            temp = curmax * num
            curmax = max(num, num * curmax, num * curmin)
            curmin = min(num, temp, num * curmin)
            res = max(res, curmax)
        
        return res