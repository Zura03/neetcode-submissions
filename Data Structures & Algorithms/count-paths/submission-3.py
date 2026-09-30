class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n

        for r in range(m - 1, -1, -1):
            cur = [0] * n
            cur[n - 1] = 1
            for c in range(n - 2, -1, -1):
                cur[c] = cur[c + 1] + prev[c]
            prev = cur

        return cur[0]