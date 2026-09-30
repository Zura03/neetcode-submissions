class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L, R = 0, 0
        res = 0

        while R < len(s):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            R += 1
            res = max(res, R - L)

        return res