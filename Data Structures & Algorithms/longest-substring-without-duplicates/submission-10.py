class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curSet = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1
            curSet.add(s[r])
            r += 1
            res = max(res, r - l)
        return res

            