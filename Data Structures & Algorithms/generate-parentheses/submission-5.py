class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(op, close, subres):
            if op == n and close == n:
                res.append(subres)
                return

            if op < n:
                dfs(op + 1, close, subres + "(")

            if close < op:
                dfs(op, close + 1, subres + ")")

        dfs(0, 0, "")
        return res