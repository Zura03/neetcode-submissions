class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
                if j == len(s):
                    return res
            L = int(s[i:j])
            subres = s[j+1:j+L+1]
            res.append(subres)
            i = j + L + 1
        return res