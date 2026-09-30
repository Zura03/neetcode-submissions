class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, L, R):
        while L < R:
            if s[L] != s[R]:
                return False
            L, R = L + 1, R - 1
        return True