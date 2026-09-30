class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, curSet):
            if i == len(nums):
                res.append(curSet.copy())
                return

            #include atleast 1 nums[i]
            curSet.append(nums[i])
            backtrack(i + 1, curSet)
            curSet.pop()

            #exclude 'nums[i]'
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curSet)

        backtrack(0, [])
        return res