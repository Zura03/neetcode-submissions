class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack, res = [], []

        def helper(closeN, openN):
            if closeN == openN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append('(')
                helper(closeN, openN + 1)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                helper(closeN + 1, openN)
                stack.pop()

        helper(0, 0)
        return res