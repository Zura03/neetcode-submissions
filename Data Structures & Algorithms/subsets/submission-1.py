class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subRes):
            if i >= len(nums):
                res.append(subRes.copy())
                return

            subRes.append(nums[i])
            dfs(i + 1, subRes)
            subRes.pop()

            dfs(i + 1, subRes)

        dfs(0, [])
        return res

            