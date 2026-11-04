class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lmap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        res = []
        subres = ""

        def dfs(i):
            nonlocal subres

            if i == len(digits):
                res.append(subres)
                return

            for c in lmap[digits[i]]:
                subres += c
                dfs(i+1)
                subres = subres[:len(subres) - 1]
        
        dfs(0)
        return res if res[0] != "" else []