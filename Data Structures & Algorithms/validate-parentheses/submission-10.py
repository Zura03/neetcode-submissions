class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {
            ")" : "(" ,
            "]" : "[" ,
            "}" : "{"
        }

        stack = []

        for c in s:
            if c not in pmap:
                stack.append(c)
            else:
                if stack and pmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False

