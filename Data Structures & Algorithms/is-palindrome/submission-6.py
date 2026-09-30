class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNumeric(s, i):
            return ((ord('a') <= ord(s[i]) <= ord('z')) or 
                    (ord('A') <= ord(s[i]) <= ord('Z')) or
                    (ord('0') <= ord(s[i]) <= ord('9')))

        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not isAlphaNumeric(s, L):
                L += 1
            while R > L and not isAlphaNumeric(s, R):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True


            

