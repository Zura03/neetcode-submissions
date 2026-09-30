class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        chars = set()
        res = 0
        while R < len(s):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            chars.add(s[R])
            res = max(res, R - L + 1)
            R += 1
        return res