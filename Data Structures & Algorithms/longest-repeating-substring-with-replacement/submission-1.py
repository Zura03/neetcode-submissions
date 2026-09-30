class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        freq = {}
        maxf = 0
        res = 0

        while R < len(s):
            freq[s[R]] = 1 + freq.get(s[R], 0)
            maxf = max(maxf, freq[s[R]])

            while (R - L + 1) - maxf > k:
                freq[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
            R += 1

        return res
            