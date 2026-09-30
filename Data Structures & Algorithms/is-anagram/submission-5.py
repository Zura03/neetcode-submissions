class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            temp[index] += 1 
        for c in t:
            index = ord(c) - ord('a')
            temp[index] -= 1
        for t in temp:
            if t != 0:
                return False
        return True