class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            res[tuple(temp)].append(s)

        r = []
        for key, val in res.items():
            r.append(val)
        return r