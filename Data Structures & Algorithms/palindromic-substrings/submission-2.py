class Solution:
    def countSubstrings(self, s: str) -> int:
        res, maxlen = 0, 0

        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > maxlen:
                    maxlen = R - L + 1
                res += 1
                L -= 1
                R += 1

            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > maxlen:
                    maxlen = R - L + 1
                res += 1
                L -= 1
                R += 1

        return res