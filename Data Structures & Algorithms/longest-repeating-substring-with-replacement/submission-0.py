class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        L, maxf = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - L + 1) - maxf > k:
                count[s[L]] -= 1
                L += 1
            
        return r - L + 1