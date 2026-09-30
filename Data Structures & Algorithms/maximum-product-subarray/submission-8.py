class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curmin, curmax = 1, 1

        for num in nums:
            if num == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * num
            curmax = max(curmax * num, curmin * num, num)
            curmin = min(curmin * num, temp, num)
            res = max(res, curmax)
            
        return res