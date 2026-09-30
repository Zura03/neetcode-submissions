class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        for num in nums:
            if num - 1 not in hashset:
                length = 0
                while num + length in hashset:
                    length += 1
                res = max(res, length)
        return res
            
