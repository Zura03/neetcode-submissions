class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, curSum, curSet):
            if curSum == target:
                res.append(curSet.copy())
                return

            if i == len(nums) or curSum > target:
                return

            #include nums[i]
            curSet.append(nums[i])
            backtrack(i, curSum + nums[i], curSet)
            curSet.pop()

            #exclude nums[i]
            backtrack(i + 1, curSum, curSet)

        backtrack(0, 0, [])
        return res