class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalin(s):
            L, R = 0, len(s) - 1
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        res, part = [], []
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPalin(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
                
        dfs(0)
        return res