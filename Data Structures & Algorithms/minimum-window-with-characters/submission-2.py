class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        L, R = 0, 0
        res, reslen = [-1, -1], float("inf")
        have, need = 0, len(countT)

        while R < len(s):

            if s[R] in countT:
                window[s[R]] = 1 + window.get(s[R], 0)
                if countT[s[R]] == window[s[R]]:
                    have += 1
                    while have == need:
                        sub_res, sub_reslen = [L, R], R - L + 1
                        if sub_reslen < reslen:
                            res, reslen = sub_res, sub_reslen
                        if s[L] in countT:
                            window[s[L]] -= 1
                            if window[s[L]] < countT[s[L]]:
                                have -= 1
                        L += 1
                
            R += 1

        return s[res[0]:res[1]+1] if reslen != float("infinity") else ""