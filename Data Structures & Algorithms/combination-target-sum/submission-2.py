class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, subRes = [], []
        def dfs(i, Sum):
            if i >= len(nums) or Sum > target:
                return
            
            if Sum == target:
                res.append(subRes.copy())
                return

            subRes.append(nums[i])
            dfs(i, Sum + nums[i])
            subRes.pop()

            dfs(i + 1, Sum)

        dfs(0, 0)
        return res

    