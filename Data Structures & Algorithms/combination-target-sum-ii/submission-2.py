class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subres = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(subres.copy())
                return
            
            if i >= len(candidates) or curSum > target:
                return

            subres.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            subres.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res