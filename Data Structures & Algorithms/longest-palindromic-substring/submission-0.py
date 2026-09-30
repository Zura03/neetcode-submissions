class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0

        def isPalindrome(L, R):
            nonlocal resLen, resIdx
            
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > resLen:
                    resIdx = L
                    resLen = R - L + 1
                L -= 1
                R += 1

        for i in range(len(s)):
            #odd length
            L, R = i, i
            isPalindrome(L, R)

            #even 
            L, R = i, i + 1
            isPalindrome(L, R)

        return s[resIdx: resIdx + resLen]