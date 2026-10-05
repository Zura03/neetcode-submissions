class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nset:
                i = 0
                L = 0
                while num + i in nset:
                    L += 1
                    i += 1
                longest = max(longest, L)
        return longest