class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]

            res = 0
            res += dfs(i + 1)
            if s[i] == '1' and i + 1 < len(s):
                res += dfs(i + 2)
            elif s[i] == '2' and i + 1 < len(s) and s[i + 1] in "0123456":
                res += dfs(i + 2)
            cache[i] = res
            return cache[i]

        return dfs(0)