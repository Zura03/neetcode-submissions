class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, subRes = [], []

        def dfs(i, Sum):
            if Sum == target:
                res.append(subRes.copy())
                return
                
            if i == len(candidates) or Sum > target:
                return


            subRes.append(candidates[i])
            dfs(i + 1, Sum + candidates[i])
            subRes.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, Sum)

        dfs(0, 0)
        return res

        